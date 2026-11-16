# Validation Report — Contract Risk Scanner

Subject: output/risk_report.md (run of input/sample_contract.txt, 2026-11-16), checked against input/sample_contract.txt, CLAUDE.md and coordinator.md.

## 1. Correctness — rating and any unsupported findings
**Rating: High.** Every excerpt is verbatim, and all section references, figures, party names and the governing law are correct. Nothing is fabricated, and the High rating and `GATE: FAIL` are supported by the contract. The weaknesses are a few over-reaching severity or interpretation calls.

Unsupported or interpretive:
- P1 "Possible punitive penalty (late-payment interest, §2.1)": the contract states a 1.5% monthly rate and never calls it a penalty. The report itself admits "punitive" is a judgment, yet it sits in the P1 table.
- P2 "Customer data ownership ambiguity (§5.1)": §5.1 is explicit ("retains no further rights", "irrevocably assigned"). Calling Customer's residual position undefined is interpretation, and the finding duplicates the P1 §5.1 finding.
- §6.2 row: "so the regime is one-sided" is the report's own inference from §6.1 and §6.2.
- §10 row: the "though Vendor is registered in England and Wales" contrast is the report's framing.
- Critical Summary: "strike or rewrite §5.1" and "negotiate a cap" are advice, not contract content (CLAUDE.md: no interpretations not in the contract text).
- Key Obligations, confidentiality (§7): paraphrased as "non-public information" without the contract's limit to information "marked confidential or would reasonably be understood to be confidential".

## 2. Completeness — gaps against the spec
No required element is missing. Present: H1 title with vendor name, Risk Rating, P1/P2/P3 tables with Clause type / Excerpt / Risk explanation / Confidence (value and reason on every row), Key Obligations for both parties, Run Info (input file, date, model, sub-agents) and a closing `GATE: FAIL`. The section order is correct.

Deviations rather than gaps:
- An extra `## Critical Summary` section sits outside the coordinator.md template and merge order.
- Run Info has an extra "Coordinator edits" line. It records that a clause-agent finding (§6.1 "uncapped") was dropped and §5.2 was folded into §5.1, which conflicts with coordinator.md step 3, "do not rewrite or paraphrase any finding".
- CLAUDE.md specifies three table columns and coordinator.md four. The report follows coordinator.md.
- Content omissions: late-payment interest (§2.1) is not in Customer's obligations, and the 12-month Initial Term (§3.1) is not mentioned.

## 3. Robustness — broken-input result before the fix
Test: coordinator run on `input/broken_input.txt`, which holds a single line of gibberish (`zx9 ;;; ### ??? lorem 0000 <<>>`). An earlier run, when the file did not yet exist, was also checked.
- The app did not crash. It launched no sub-agents and wrote nothing to `output/`, and the existing `output/risk_report.md` was left untouched.
- The reply was the one-line `ERROR: input/broken_input.txt contains no recognisable contract language (no named parties, obligations or term).`
- That was already graceful, but only because the model followed prose in coordinator.md step 0 and judged "recognisable contract language" itself. The reason text and the verdict were not guaranteed to be the same on every run, and nothing could be tested automatically.

## Issue Fixed — problem, change made, evidence from the re-run
**Problem:** input validation depended on model judgment. The same garbage, empty or borderline file could be accepted on one run and rejected on another. A wrongly accepted file would send sub-agents to invent findings, and could end in a spurious `GATE: PASS`.

**Change made:**
- Added `output/validate_input.py`, a read-only script. It checks that the file exists, is readable UTF-8 text, is non-empty, and contains at least 3 of 5 contract-language signals (agreement/contract, "shall", party wording, term/termination, payment). It prints `OK` or one `ERROR: <reason>` line and exits non-zero on failure.
- Changed coordinator.md step 0 to run `python output/validate_input.py <input path>` and to stop with exactly its output line on failure.
- The script lives in `output/` because a project hook, per CLAUDE.md, blocks writes outside that folder. coordinator.md was edited with your explicit approval.

**Evidence from the re-run** (`output/risk_report.md` SHA-1 `5af30dc7…` was identical before and after all runs):

| Input | Output | Exit |
|---|---|---|
| input/broken_input.txt | `ERROR: input/broken_input.txt contains no recognisable contract language (found 0 of 3 required signals: parties, obligations, term).` | 1 |
| input/nope.txt (missing) | `ERROR: input/nope.txt does not exist or is not a file.` | 1 |
| empty temp file | `ERROR: <path> is empty.` | 1 |
| input/sample_contract.txt | `OK` | 0 |

**Result:** the verdict now comes from deterministic code. The error message is more specific, giving the signal count, and the real contract still passes. Behaviour on the garbage input is unchanged, because it was already rejected, but it is now repeatable and testable.

**Caveats:** the keyword heuristic could wrongly accept non-contract prose that happens to use words like "party" and "shall", and could reject a very short real contract. Only the four cases above were tested. The coordinator step that calls the script was exercised by running the script directly, not by a full end-to-end agent run.
