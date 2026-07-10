# Technical Textile Defect Taxonomy v0.1

**Status:** Draft for Quality, Production, Packaging, and R&D workshop  
**Purpose:** create a controlled, versioned language for inspection, rework, scrap, root-cause analysis, and future model training.

This taxonomy is intentionally generic. It must be reconciled with actual Darmstädter/Klevers terminology, ELSIS labels, product families, and customer specifications before operational use.

## 1. Taxonomy rules

Every defect event should contain:

- one primary defect code;
- optional secondary codes;
- original source label preserved;
- defect location and size where available;
- severity;
- confidence/source;
- human disposition;
- suspected and confirmed cause kept separate;
- taxonomy version.

Do not encode cause inside the defect name. For example, `COATING_VOID` describes an observed condition; `low viscosity` or `contamination` belongs in the cause analysis.

## 2. Top-level families

| Prefix | Family | Description |
|---|---|---|
| SUB | Substrate / textile structure | Defects originating in or visible through the base fabric, mat, tape, or reinforcement |
| COA | Coating coverage and appearance | Missing, uneven, excessive, or visually inconsistent coating |
| ADH | Adhesion / interlayer integrity | Poor bonding, delamination, blistering, peeling |
| CUR | Drying / curing / blocking | Under-cure, over-cure, tack, blocking, embrittlement |
| SUR | Surface contamination and marks | Dirt, oil, foreign matter, stains, impressions |
| GEO | Geometry and dimensional | Width, thickness, weight, skew, edge, wrinkles, deformation |
| COL | Color and optical | Color variation, streaks, gloss, opacity |
| LAM | Lamination / foil / film | Bubbles, wrinkles, lifting, misalignment, foil damage |
| MEC | Mechanical damage | Holes, tears, cuts, abrasion, crushing |
| THM | Thermal / fire performance | Thermal degradation, flame-test failure, smoke/char anomalies |
| PKG | Packaging / winding | Poor winding, telescoping, creases, roll damage, labeling |
| DOC | Documentation / traceability | Missing label, wrong article, missing test/certificate, identifier mismatch |
| UNK | Unknown / unclassified | Temporary category requiring review |

## 3. Initial controlled codes

### SUB — substrate / textile structure

| Code | Name | Observable definition |
|---|---|---|
| SUB-BROKEN-YARN | Broken yarn | One or more yarns visibly interrupted |
| SUB-MISSING-YARN | Missing yarn | Expected yarn absent over a measurable length/area |
| SUB-YARN-DISTORTION | Yarn distortion | Local displacement, bunching, spreading, or waviness |
| SUB-WEAVE-DEFECT | Weave defect | Incorrect interlacing pattern or structural irregularity |
| SUB-NEEDLEMAT-NONUNIFORM | Needlemat non-uniformity | Local density/thickness variation in mat |
| SUB-SEAM-JOIN | Seam or join anomaly | Join/splice outside acceptance criteria |
| SUB-OPEN-AREA | Excessive open area | Local pore/opening larger than approved expectation |

### COA — coating coverage and appearance

| Code | Name | Observable definition |
|---|---|---|
| COA-MISSING | Missing coating | Substrate area not covered where coating is required |
| COA-THIN | Locally thin coating | Coverage or opacity visibly/measurably below expectation |
| COA-EXCESS | Excess coating | Local accumulation, ridge, pool, or excessive add-on |
| COA-UNEVEN | Uneven coating | Non-uniform coating distribution without a more specific code |
| COA-STREAK | Coating streak | Continuous longitudinal or transverse band variation |
| COA-PINHOLE | Pinhole | Small isolated opening through coating |
| COA-VOID | Coating void | Larger uncoated opening or cavity |
| COA-FISHEYE | Fisheye / crater | Circular depression or repelled area |
| COA-FOAM-BUBBLE | Foam/bubble mark | Bubble-origin surface or internal void |
| COA-DRIP | Drip / run | Flow mark caused by local coating movement |
| COA-EDGE-BUILDUP | Edge buildup | Excess coating accumulation near edge |
| COA-PRINT-THROUGH | Substrate print-through | Textile structure excessively visible through finish |

### ADH — adhesion / interlayer integrity

| Code | Name | Observable definition |
|---|---|---|
| ADH-POOR | Poor adhesion | Coating or layer separates below acceptance requirement |
| ADH-DELAMINATION | Delamination | Separation between laminated/coated layers |
| ADH-PEELING | Peeling | Progressive visible layer detachment |
| ADH-BLISTER | Blister | Raised area caused by local interlayer separation or trapped gas |
| ADH-EDGE-LIFT | Edge lifting | Layer separation initiated at an edge |

### CUR — drying / curing / blocking

| Code | Name | Observable definition |
|---|---|---|
| CUR-TACKY | Tacky surface | Surface remains undesirably sticky |
| CUR-BLOCKING | Blocking | Adjacent wound/contact surfaces adhere unintentionally |
| CUR-UNDERCURE | Suspected under-cure | Approved evidence indicates incomplete cure; use only with test/process support |
| CUR-OVERCURE | Suspected over-cure | Approved evidence indicates excessive cure/thermal exposure |
| CUR-BRITTLE | Embrittlement | Material loses required flexibility after processing/aging |
| CUR-CRACK | Cure-related cracking | Cracks associated with bending, winding, or aging |

### SUR — contamination and marks

| Code | Name | Observable definition |
|---|---|---|
| SUR-DIRT | Dirt | Visible particulate contamination |
| SUR-OIL | Oil/grease mark | Local oily or greasy contamination |
| SUR-FOREIGN-MATERIAL | Foreign material | Embedded or attached material not belonging to product |
| SUR-STAIN | Stain | Discoloration not classified as normal color variation |
| SUR-ROLLER-MARK | Roller impression | Repeating or localized surface mark associated with contact |
| SUR-SCRATCH | Scratch | Linear surface damage not penetrating as a cut |

### GEO — geometry and dimensions

| Code | Name | Observable definition |
|---|---|---|
| GEO-WIDTH-LOW | Width below limit | Measured width below approved lower limit |
| GEO-WIDTH-HIGH | Width above limit | Measured width above approved upper limit |
| GEO-THICKNESS-LOW | Thickness below limit | Measured thickness below approved lower limit |
| GEO-THICKNESS-HIGH | Thickness above limit | Measured thickness above approved upper limit |
| GEO-WEIGHT-LOW | Area weight below limit | Measured mass/area below lower limit |
| GEO-WEIGHT-HIGH | Area weight above limit | Measured mass/area above upper limit |
| GEO-WRINKLE | Wrinkle | Fold or crease formed during processing/winding |
| GEO-SKEW | Skew / distortion | Textile geometry deviates from approved alignment |
| GEO-CURL | Curl | Edge or sheet curls outside expected flatness |
| GEO-EDGE-IRREGULAR | Irregular edge | Edge is frayed, wavy, damaged, or dimensionally unstable |

### COL — color and optical

| Code | Name | Observable definition |
|---|---|---|
| COL-MISMATCH | Color mismatch | Overall color outside approved reference/tolerance |
| COL-VARIATION | Local color variation | Uneven shade within roll/material |
| COL-STREAK | Color streak | Directional band of shade difference |
| COL-GLOSS | Gloss variation | Local or overall gloss outside expectation |
| COL-OPACITY | Opacity variation | Transparency/coverage differs from expectation |

### LAM — lamination / foil / film

| Code | Name | Observable definition |
|---|---|---|
| LAM-BUBBLE | Lamination bubble | Trapped air/gas creating a raised area |
| LAM-WRINKLE | Lamination wrinkle | Wrinkle in film, foil, or bonded layer |
| LAM-MISALIGN | Layer misalignment | Laminate/foil position outside tolerance |
| LAM-LIFT | Layer lifting | Partial separation without full delamination |
| LAM-FOIL-TEAR | Foil tear | Tear or rupture in foil layer |
| LAM-FOIL-PINHOLE | Foil pinhole | Small perforation in foil layer |
| LAM-ADHESIVE-BLEED | Adhesive bleed | Adhesive visible beyond intended region or through layer |

### MEC — mechanical damage

| Code | Name | Observable definition |
|---|---|---|
| MEC-HOLE | Hole | Through-thickness opening not explained by intended structure |
| MEC-TEAR | Tear | Irregular rupture propagated through material |
| MEC-CUT | Cut | Sharp linear separation |
| MEC-ABRASION | Abrasion damage | Surface/material loss caused by rubbing |
| MEC-CRUSH | Compression/crush damage | Permanent local compression or deformation |
| MEC-EDGE-DAMAGE | Edge damage | Mechanical damage limited to edge zone |

### THM — thermal / fire performance

| Code | Name | Observable definition |
|---|---|---|
| THM-DISCOLORATION | Thermal discoloration | Color change after thermal exposure beyond approved expectation |
| THM-HARDENING | Thermal hardening | Loss of flexibility after thermal exposure |
| THM-CRACKING | Thermal cracking | Cracks after heat/aging exposure |
| THM-DELAMINATION | Thermal delamination | Layer separation after thermal exposure |
| THM-FLAME-FAIL | Flame-test failure | Approved flame-test criterion not met |
| THM-SMOKE-FAIL | Smoke criterion failure | Approved smoke criterion not met |
| THM-CHAR-ANOMALY | Char anomaly | Unexpected char behavior in approved test |

### PKG — packaging / winding

| Code | Name | Observable definition |
|---|---|---|
| PKG-TELESCOPING | Telescoping | Roll layers shift axially |
| PKG-LOOSE-WIND | Loose winding | Insufficient roll tension or unstable package |
| PKG-TIGHT-WIND | Excessively tight winding | Compression/impression/damage associated with excessive winding tension |
| PKG-CREASE | Packaging crease | Crease introduced during winding/handling/packaging |
| PKG-CORE-DAMAGE | Core damage | Bent, crushed, broken, or unsuitable core |
| PKG-ROLL-DAMAGE | Roll handling damage | External roll damage not otherwise classified |
| PKG-WRAP-DAMAGE | Packaging wrap damage | Protective packaging is damaged or inadequate |
| PKG-LABEL-MISSING | Missing label | Required roll/package label absent |
| PKG-LABEL-WRONG | Incorrect label | Label content conflicts with actual product/order |

### DOC — documentation / traceability

| Code | Name | Observable definition |
|---|---|---|
| DOC-ID-MISMATCH | Identifier mismatch | Roll/order/article/batch identifiers conflict across sources |
| DOC-TEST-MISSING | Required test missing | Required QC/lab evidence unavailable |
| DOC-CERT-MISSING | Required certificate missing | Required certificate/evidence unavailable |
| DOC-RECORD-INCOMPLETE | Incomplete record | Required fields or approvals missing |
| DOC-REVISION-WRONG | Wrong revision | Outdated/incorrect specification, recipe, method, or document used |

## 4. Severity model

Severity should be defined by product/customer requirements. Initial generic scale:

| Level | Name | Generic meaning |
|---:|---|---|
| 0 | Informational | Observation; no quality impact |
| 1 | Minor | Cosmetic/local; within acceptance or no action needed |
| 2 | Moderate | Requires review, marking, local action, or conditional acceptance |
| 3 | Major | Rework, downgrade, hold, or significant customer risk |
| 4 | Critical | Safety, compliance, functional failure, rejection, major complaint, or mandatory scrap |

Severity is not the same as system confidence.

## 5. Disposition codes

- `ACCEPT`
- `ACCEPT_WITH_DEVIATION`
- `MARK`
- `CUT_OUT`
- `REWORK`
- `RETEST`
- `HOLD`
- `DOWNGRADE`
- `SCRAP`
- `REJECT`
- `UNKNOWN`

## 6. Cause status

| Status | Meaning |
|---|---|
| `UNKNOWN` | No cause assessment yet |
| `HYPOTHESIS` | Plausible cause proposed but not verified |
| `SUPPORTED` | Multiple evidence sources support the cause |
| `CONFIRMED` | Cause verified through investigation, experiment, or approved evidence |
| `DISPROVED` | Hypothesis tested and rejected |

## 7. Cause families

Use a separate cause taxonomy:

- material/substrate variation;
- raw-material/supplier lot;
- formulation/mixing;
- viscosity/solids/pot life;
- contamination;
- line speed;
- temperature/drying/curing;
- tension/web handling;
- coating gap/application;
- lamination pressure/temperature;
- environment/humidity;
- equipment/maintenance;
- inspection/classification error;
- handling/packaging;
- specification/documentation;
- unknown.

## 8. Taxonomy workshop outputs

The first workshop should produce:

1. mapping of every current ELSIS label to v0.1 or a new code;
2. mapping of QC, production, complaint, and rework terms;
3. top 20 high-frequency/high-cost defect definitions;
4. approved severity rules by pilot product family;
5. image examples and counterexamples where available;
6. disposition rules;
7. owners and review cadence;
8. taxonomy v1.0 approval.

## 9. Governance

- Quality owns the approved defect definitions.
- Packaging/inspection owns operational labeling guidance.
- Production and R&D review technical meaning and cause hypotheses.
- IT/AI maintains machine-readable codes and version history.
- Historical source labels are never deleted; they are mapped to controlled codes.
- Changes require a version increment and documented migration rule.