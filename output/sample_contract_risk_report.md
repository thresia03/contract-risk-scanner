# Contract Risk Report: sample_contract.txt

## Overall Risk Rating
**High** — multiple P1 findings.

## P1 Critical Findings
| Clause type | Excerpt | Risk explanation |
|---|---|---|
| Auto-renewal without adequate notice (§3.2) | "automatically renew for successive periods of twelve (12) months unless Customer provides written notice of non-renewal at least seven (7) days prior to the end of the then-current term. Failure to give timely notice shall bind Customer to the full renewal fee." | Renews automatically for 12 months; only a 7-day notice window to prevent it, with the full renewal fee owed if missed. |
| Uncapped liability (§6.2) | "Customer's liability to Vendor ... shall be unlimited and shall include all direct and indirect losses, costs, and expenses incurred by Vendor." | Customer's liability has no cap and includes indirect losses, while Vendor's liability excludes indirect and consequential damages, loss of profits and loss of data (§6.1). |
| Unilateral data assignment to vendor (§5.1, §5.2) | "All data, content, records, and information uploaded to or generated through the Services ... is hereby irrevocably assigned to Vendor." / "Vendor may use, analyse, aggregate, license, and commercialise Customer Data ... during and after the term" | All Customer Data is irrevocably assigned to Vendor, which may commercialise it during and after the term without notice or compensation. |

## P2 Major Findings
| Clause type | Excerpt | Risk explanation |
|---|---|---|
| Price escalation trigger (§2.2) | "Vendor may increase the subscription fees by up to fifteen percent (15%) in each contract year ... without the need for Customer's consent or approval." | Vendor may raise fees by up to 15% every contract year without Customer's consent. |
| Broad indemnification (§6.3) | "Customer shall indemnify and hold harmless Vendor against all claims arising from Customer's use of the Services." | Indemnity covers all claims arising from use of the Services; no limit or exclusions are stated. |
| Customer data ownership ambiguity (§5.1) | "Customer retains no further rights in data once submitted, as set out below." | Customer's retained rights in its data are stated only as "no further rights". |

## P3 Minor Findings
| Clause type | Excerpt | Risk explanation |
|---|---|---|
| Notice period (§3.2) | "at least seven (7) days prior to the end of the then-current term" | Very short non-renewal notice period (also the basis of the P1 renewal finding). |
| Termination for convenience (§4.1) | "Either party may terminate this Agreement for convenience by giving thirty (30) days' prior written notice" | Mutual 30-day notice. §4.3 states no refunds are due for prepaid fees. |
| Governing law / forum (§10) | "governed by ... the laws of the State of Delaware ... exclusive jurisdiction of the state and federal courts located in Delaware." | Delaware law and exclusive Delaware courts. |

## Key Obligations
### Customer (Acme Corp)
- Pay the annual subscription fee within 30 days of invoice; late amounts accrue interest at 1.5% per month (§2.1).
- Pay fees accrued through termination; no refunds of prepaid fees (§4.3).
- Give written non-renewal notice at least 7 days before the end of each term to avoid renewal (§3.2).
- Indemnify Vendor against all claims arising from use of the Services (§6.3).
- Keep Vendor's confidential information confidential for 3 years after termination (§7).
- Use the Services only under a limited, non-exclusive, non-transferable right during the term (§8).

### Vendor (TechVendor Ltd.)
- Provide access to the Services per Schedule A, using commercially reasonable efforts for 99.5% monthly availability, excluding scheduled maintenance (§1).
- Keep Customer's confidential information confidential for 3 years after termination (§7).
- Cure material breach within 15 days of notice, or face termination (§4.2).

## Notes
- Schedules A and B are referenced but not included in the text, so the fee amount and service scope are not stated.
- The signature block is unsigned and undated.
- Services are provided "as is" with all warranties disclaimed (§9). Vendor may assign the agreement to an affiliate or successor without consent (§11).

GATE: FAIL
