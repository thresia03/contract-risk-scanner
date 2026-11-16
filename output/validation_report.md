# Validation Report — Contract Risk Scanner

Subject: output/risk_report.md (run of input/sample_contract.txt, 2026-11-14), checked against input/sample_contract.txt, CLAUDE.md and coordinator.md.

## 1. Correctness — rating and any unsupported findings
**Rating: Medium.** All excerpts are verbatim, party names and figures are correct, and the High rating and GATE: FAIL are supported by the contract. Several rows are over-classified or add interpretation the contract does not contain, which CLAUDE.md forbids.

Unsupported or overstated:
- P1 "Late-payment interest (2.1)": the contract says "interest", never "penalty". Not a P1 finding on the text.
- P1 "Vendor retention of improvements and derivative works (8)": the clause says "retains", not "assigns", so it does not fit the unilateral-assignment category.
- P1 "Vendor liability with no stated cap (6.1)": the contract states neither a cap nor "uncapped"; "potentially very limited" is the report's own reading.
- P2 "Customer data ownership ambiguity (5.1)": the claim that it "conflicts with" 5.2 and is "internally inconsistent" is unsupported; 5.1 and 5.2 agree that Vendor takes the data. High confidence is overstated.
- P3 "Governing law (10)": "Cross-border enforcement may be harder to predict" is not in the contract.
- P3 "Confidentiality survival (7)": "Information disclosed later may fall outside protection" is unclear and unsupported.
- P3 "Non-refundable prepaid fees (4.3)": "even where Vendor is at fault" goes beyond the text.
- P3 (4.1, 4.2): "short window to find a replacement" and "may limit Customer's ability to remedy" are commentary.
- Key Obligations: Section 4.1 (termination for convenience) is a right, and Section 6.1 (Vendor's damages exclusion) is a limitation; neither is an obligation.

## 2. Completeness — gaps against the spec
No required element is missing. Present: H1 title, Risk Rating, P1/P2/P3 tables with Clause type / Excerpt / Risk explanation / Confidence (value plus reason on every row), Key Obligations for both parties, Run Info (input file, date, model, sub-agents), and a final `GATE: FAIL`.

Deviations rather than gaps:
- A Critical Summary paragraph is included that the spec does not define.
- Four rows fall outside the P1/P2/P3 taxonomy: Section 11 assignment, Section 9 warranties, Section 4.3 prepaid refunds, Section 7 confidentiality survival.
- Key Obligations omits the mutual no-assignment-without-consent duty (Section 11).
- Obligation-agent and risk-agent have no table rows, so the Confidence column applies only to clause-agent output.

## 3. Robustness — broken-input result before the fix
Test: `claude -p "Follow coordinator.md for input/broken_input.txt"`. The file does not exist (`input/` holds only `sample_contract.txt`).
- The app did not crash and launched no sub-agents.
- `output/risk_report.md` was left unchanged (identical checksum before and after).
- The reply was free-form: it explained the file was missing and asked the user which option they wanted. The graceful behaviour came from model judgment, not from the spec, so the format was not guaranteed and nothing covered empty or non-contract files.
- The empty/garbage-file case was not tested before the fix.

## Issue Fixed — problem, change made, evidence from the re-run
**Problem:** coordinator.md had no input validation. Behaviour on a missing, empty or non-contract file depended on model judgment, so a garbage file could lead to sub-agents inventing findings or a spurious `GATE: PASS`.

**Change made (coordinator.md, new Step 0):** validate the input first. If the file is missing, empty, or has no recognisable contract language (named parties, obligations, term), launch no sub-agents, write nothing to output/, and reply with exactly one line `ERROR: <reason>` with no GATE line.

**Evidence from the re-run** (`output/risk_report.md` checksum unchanged in both runs; no sub-agents launched):
- Missing file, `input/broken_input.txt` → `ERROR: input/broken_input.txt does not exist, so there is no contract to analyse.`
- Garbage file (`output/_garbage_test.txt`, random text, created for the test and deleted afterwards) → `ERROR: input/output/_garbage_test.txt contains no recognisable contract language (no named parties, obligations, or term).`

**Result:** the missing-file case now returns a fixed one-line error instead of a free-form question, and the garbage-file case is rejected rather than analysed. The new behaviour is only checked on these two cases.

**Remaining caveat:** the garbage-file message printed the path as `input/output/_garbage_test.txt`, because the coordinator prefixed `input/` to the path given. The rejection is correct; the path shown in the message is not.
