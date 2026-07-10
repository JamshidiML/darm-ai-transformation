# Executive AI Transformation Discovery & Strategy Report

**Company:** Darmstädter GmbH and Klevers GmbH & Co. KG  
**Prepared for:** Internal R&D AI champion  
**Date:** 2026-07-02  
**Objective:** Secure management approval for a measurable AI pilot, then build the foundations for an Industrial AI Platform.

---

## Executive Thesis

Darmstädter and Klevers are not ordinary textile manufacturers. Public company material shows a high-mix, function-first technical textile group built on coatings, appretures, laminations, hybrid articles, glass and aramid fabrics, high-temperature yarns, needlemats, tapes, lab testing, certification, and customer-specific development. The strongest AI opportunity is therefore not "automation" in the abstract. It is the conversion of decades of material, process, quality, certification, supplier, and application knowledge into a repeatable decision system.

The recommended first move is a **12-week read-only Coating and Packaging Quality Intelligence pilot** around one product family or production line. The pilot should link order/roll context, process parameters, inspection results, lab/QC results, and operator notes into one traceable quality picture. It should not change machine control in phase 1. The business promise is practical: lower scrap and rework, faster root cause analysis, fewer repeated defects, better customer complaint response, and a credible data spine for later R&D formulation AI.

The long-term prize is larger: a proprietary Industrial AI Platform for technical textiles that can recommend formulations, predict quality risk before shipment, capture expert knowledge, accelerate customer-specific product development, and defend the company's competitive position against lower-cost commodity suppliers.

---

## Evidence Base And Source Notes

This report is grounded in public sources available as of 2026-07-02 plus clearly marked internal-context assumptions.

Key public facts:

- Darmstädter was founded in 1952, began with protective-clothing confection, and shifted toward refinement of glass fabrics, aramid fabrics, and blends. It states that its machine park ranges from coating systems to special machine construction and that products are used worldwide in automotive, shipbuilding, aviation, power-plant, expansion-joint, high-temperature insulation, protective clothing, and fire/smoke protection applications. Source: [Darmstädter Unternehmen](https://www.darmstaedter.eu/unternehmen/).
- Darmstädter coating capabilities include silicone, PU/PVA/PAC, vermiculite, and expandable graphite systems, including silicone to 260°C or special silicones to 300°C, vermiculite up to 1200°C depending on substrate, transfer coating for smooth surfaces, multi-layer coatings, and flame-protection standards. Source: [Darmstädter Beschichtungen](https://www.darmstaedter.eu/beschichtungen/).
- Darmstädter states that its quality lab tests width, weight, thickness, long-term temperature behavior, water column, bend tests, flame tests, tensile strength, and tear propagation; it also references ISO 9001 and Module D quality assurance under the EU Marine Equipment Directive. Source: [Darmstädter Qualität](https://www.darmstaedter.eu/qualitaet/).
- Darmstädter describes an R&D lab that mirrors large production equipment at small scale and is supported by chemical suppliers, research institutions, and qualified suppliers. Source: [Darmstädter Entwicklung](https://www.darmstaedter.eu/entwicklung/).
- Klevers was founded in 1923 as a silk weaving mill and has focused on technical textiles since 1938. It describes itself as a third-generation family company developing tailored technical solutions for global customers. Source: [Klevers Unternehmen](https://klevers.de/unternehmen/).
- Klevers product pages cover yarns/twines, glass high-temperature fabrics to 1200°C, roving fabrics, aramid fabrics, special fabrics, coatings, laminations, wet finishes, needlemats, and tapes. Sources: [Klevers Produkte](https://klevers.de/produkte/), [Klevers Garne und Zwirne](https://klevers.de/garne-und-zwirne/), [Klevers Glas Hochtemperatur](https://klevers.de/glas-hochtemperatur/), [Klevers Beschichtungen](https://klevers.de/beschichtungen/), [Klevers Nadelmatten und Bänder](https://klevers.de/nadelmatten-und-baender/).
- Klevers states that, as an integrated weaving operation, it can combine raw fabrics, coatings, and laminations to create individual application-specific fabrics with support from its development department. Source: [Klevers Lieferprogramm](https://klevers.de/lieferprogramm/).
- Klevers lists ISO 9001, Module D and Module B for marine equipment, EN 13501, M1 classification, and EDF/PMUC and DCNS product approvals. Source: [Klevers Qualität](https://klevers.de/qualitaet/).
- Klevers describes public R&D projects with RWTH Aachen ITA, including ZIM CustomWeave and a basalt ceramic fiber project, plus research in glass, aramid, basalt, and carbon fiber fabric development. Source: [Klevers Projekte](https://klevers.de/projekte/).

Internal-context assumptions to verify before execution:

- Prior internal discussion indicated possible data sources such as INTEX, ELSIS inspection data, PLC/HMI data, Siemens SIMATIC, Monforts/Menzel lines, defect labels, and exportable inspection images. These are not public-source facts in this report. Treat them as a discovery checklist.
- The report avoids claiming current cost, scrap, complaint, or OEE baselines because those numbers must come from internal data.

---

## Part 1: Complete AI Opportunity Map

The company value chain can be read as six linked systems:

1. **Market need:** customer asks for a high-temperature, fire-protection, insulation, acoustic, composite, marine, automotive, or PPE textile function.
2. **Product design:** substrate, fiber, weave, coating, lamination, appreture, adhesive, foil, color, finish, and certification requirements are combined.
3. **Production execution:** coating, wet finishing, lamination, thermal treatment, weaving, cutting, packaging, and inspection convert recipes into roll/product quality.
4. **Quality proof:** lab tests, external tests, certificates, standards, customer approvals, and traceability create trust.
5. **Knowledge reuse:** experts remember what worked, what failed, which supplier batch behaved differently, and which process window is robust.
6. **Commercial conversion:** sales turns technical capability into quotations, samples, approvals, repeat orders, and long customer relationships.

AI creates value wherever decisions are repeated, data is fragmented, expert knowledge is tacit, or quality depends on hidden combinations of material and process variables.

| Department | AI value theme | Best first opportunity | Long-term opportunity |
|---|---|---|---|
| Management | Decision intelligence | AI portfolio dashboard with value, risk, and status | AI-enabled operating model and strategy cockpit |
| Sales | Technical solution speed | Spec-to-product recommender for customer inquiries | AI-guided application engineering and margin optimization |
| Marketing | Market intelligence | Technical content assistant using approved TDS/certificates | Application-specific demand sensing and competitive radar |
| Customer Service | Complaint and request handling | Complaint triage and root-cause retrieval | Predictive complaint prevention by product/customer/application |
| Procurement | Supplier and raw-material intelligence | Alternative material/supplier search | Supplier quality and availability risk prediction |
| Supply Chain | Planning and flow | Roll/order traceability dashboard | Demand, capacity, and material optimization |
| Warehouse | Inventory accuracy | Barcode/RFID roll passport | AI inventory and aging-risk prediction |
| Maintenance | Uptime | Maintenance log assistant | Predictive maintenance and spare-part optimization |
| Production | Process stability | Process-parameter and defect correlation | Digital twin and closed-loop parameter recommendation |
| Laboratory | Faster learning | Digital lab notebook and test extraction | Experiment recommendation and formulation optimization |
| Quality Control | Quality intelligence | Roll-level quality passport | Predictive quality release and automated CAPA |
| Packaging | Inspection intelligence | Defect taxonomy and inspection analytics | Vision/process feedback loop and operator copilot |
| Finance | Cost transparency | Product/job costing analytics | Quote-to-margin AI and variance prediction |
| HR | Skills and training | Operator onboarding knowledge bot | Skills matrix, training recommendation, succession planning |
| R&D | Materials intelligence | R&D knowledge graph and experiment memory | Materials AI platform for coatings, laminations, and hybrids |
| IT | Secure enablement | Read-only data connectors and access governance | Industrial data platform with MLOps and knowledge graph |
| Compliance | Documentation | Certificate and standards assistant | Certification automation and regulatory risk monitoring |
| Safety/Environment | Risk reduction | Safety document assistant and incident trend analysis | Energy, emissions, solvent, and waste optimization |

---

## Part 2: Department-by-Department Workflow, Pain Points, Data, ROI, And Complexity

### Management

| Dimension | Assessment |
|---|---|
| Current workflow | Decisions likely rely on ERP reports, departmental updates, finance data, production meetings, customer escalations, and expert judgment. |
| Pain points | Fragmented visibility across Darmstädter and Klevers, delayed quality signals, hidden cost of rework, slow prioritization of improvement ideas. |
| Hidden inefficiencies | Problems are discussed after they become visible; repeated defects and repeated development questions may not be quantified. |
| Data sources | ERP, production logs, QC reports, complaints, sales pipeline, margin/costing, energy, maintenance, project lists. |
| AI opportunities | AI transformation dashboard, opportunity backlog, executive early-warning system, risk/ROI prioritizer. |
| Expected ROI | Medium direct ROI; high strategic ROI because management can approve the right pilots and stop weak ones early. |
| Required data | Project cost, baseline KPIs, scrap/rework, complaints, energy, cycle times, quality holds. |
| Complexity | Low to medium if existing data is exported read-only. |
| Quick win | Monthly AI value dashboard with five KPIs and pilot tracking. |
| Long-term | AI operating model with portfolio governance and funding pipeline. |
| Investment | EUR 10k-40k for first dashboard and KPI model. |
| Business impact | Faster decisions, less scattered experimentation, better executive trust. |

### Sales And Application Engineering

| Dimension | Assessment |
|---|---|
| Current workflow | Customer inquiry is interpreted by experienced sales/application people; product candidates are selected from memory, TDS, past jobs, samples, and supplier knowledge. |
| Pain points | Expert bottlenecks, slow response to complex inquiries, risk of repeating past failed combinations, inconsistent quotation assumptions. |
| Lost knowledge | Why a specific substrate/coating/lamination was selected for an application; why a similar request failed; which certificates apply. |
| Data sources | Inquiries, quotations, TDS, product PDFs, certificates, previous orders, customer industries, complaints, sample results. |
| AI opportunities | Spec-to-solution recommender, quotation assistant, approved TDS generator, "similar past projects" search, margin-risk assistant. |
| Expected ROI | High if response time and win rate improve or if low-margin custom work is priced better. |
| Required data | Product master, historical orders, quote templates, application tags, certification tags, pricing/margin rules. |
| Complexity | Medium; knowledge quality matters more than model complexity. |
| Quick win | Internal assistant that answers: "Which products have worked for this temperature/application/certification?" |
| Long-term | AI sales engineer that proposes product routes, sample plans, tests, and quotation risk levels. |
| Investment | EUR 20k-80k for knowledge assistant; EUR 100k+ for integrated quote intelligence. |
| Business impact | Faster technical sales, fewer dependency bottlenecks, better capture of premium custom value. |

### Marketing

| Dimension | Assessment |
|---|---|
| Current workflow | Product pages, PDFs, trade fair materials, technical claims, and customer references communicate capabilities. |
| Pain points | Technical content is hard to keep consistent across product families, languages, and certifications. |
| Hidden inefficiencies | Marketing may not fully exploit the company's strongest differentiator: customized combinations backed by lab and certification knowledge. |
| Data sources | Website, product PDFs, certificates, approved photos, trade fair materials, application notes. |
| AI opportunities | Approved-content assistant, application-specific landing pages, market trend monitoring, competitor radar. |
| Expected ROI | Medium; supports sales quality and brand perception. |
| Required data | Approved claims library, source-linked product facts, image rights, brand rules. |
| Complexity | Low if claims are source controlled. |
| Quick win | AI-assisted, human-approved application briefs for marine, fire protection, insulation, automotive, and PPE. |
| Long-term | Demand-sensing engine that connects market signals to product development priorities. |
| Investment | EUR 10k-50k. |
| Business impact | Stronger technical credibility and faster content creation. |

### Customer Service And Complaints

| Dimension | Assessment |
|---|---|
| Current workflow | Customer requests and complaints move through email, internal service, quality, production, and sometimes R&D. |
| Pain points | Root cause evidence is scattered; complaint response depends on people finding the right order, roll, test, or production record. |
| Lost knowledge | Similar complaint histories, corrective actions, supplier batch links, operator observations. |
| Data sources | Emails, complaints, CRM/ERP, order history, roll records, QC reports, lab tests, photos, CAPA. |
| AI opportunities | Complaint triage, similar-case retrieval, CAPA drafting, automatic evidence packet for customer response. |
| Expected ROI | High if it reduces repeated complaints or protects key accounts. |
| Required data | Complaint categories, order/roll linkage, QC records, approved response templates. |
| Complexity | Medium. |
| Quick win | Complaint knowledge search across PDFs, emails, QC documents, and TDS. |
| Long-term | Complaint prediction and proactive customer risk alerts. |
| Investment | EUR 20k-70k. |
| Business impact | Faster response, less firefighting, improved customer trust. |

### Procurement

| Dimension | Assessment |
|---|---|
| Current workflow | Suppliers provide chemicals, fibers, foils, binders, adhesives, coatings, and specialty materials. Substitution decisions require R&D and quality expertise. |
| Pain points | Supplier disruptions, price volatility, hidden quality differences, slow alternative qualification. |
| Lost knowledge | Past supplier batch behavior, formulation sensitivity, test outcomes from rejected alternatives. |
| Data sources | Supplier docs, MSDS/SDS, TDS, CoA, purchase history, lot/batch data, QC performance, complaints. |
| AI opportunities | Supplier intelligence, raw-material substitution recommender, SDS/TDS extraction, risk alerts, price anomaly detection. |
| Expected ROI | Medium to high depending on raw material volatility and qualification costs. |
| Required data | Material master, suppliers, batches, formulation usage, test outcomes. |
| Complexity | Medium to high because substitution is technically sensitive. |
| Quick win | SDS/TDS knowledge assistant and alternative supplier watchlist. |
| Long-term | AI-supported qualification plans for alternative materials. |
| Investment | EUR 20k-100k. |
| Business impact | Supply resilience, lower emergency purchasing, faster response to discontinued materials. |

### Supply Chain And Planning

| Dimension | Assessment |
|---|---|
| Current workflow | Customer orders, production capacity, raw material availability, and due dates are balanced manually or through ERP. |
| Pain points | High-mix custom orders make planning hard; quality holds and rework disrupt schedules. |
| Hidden inefficiencies | Suboptimal sequencing of coatings/colors/widths/cleaning requirements; rush jobs may create avoidable changeovers. |
| Data sources | ERP, production schedule, machine availability, order backlog, material inventory, quality holds, shipping. |
| AI opportunities | Schedule risk prediction, changeover-aware sequencing, material shortage prediction, due-date risk alerts. |
| Expected ROI | High if bottleneck utilization and OTIF improve. |
| Required data | Order routing, machine calendars, setup/changeover rules, inventory, WIP status. |
| Complexity | Medium to high. |
| Quick win | Delay-risk dashboard and bottleneck forecast. |
| Long-term | AI scheduling optimizer with human planner override. |
| Investment | EUR 40k-150k. |
| Business impact | Better delivery reliability and less firefighting. |

### Warehouse

| Dimension | Assessment |
|---|---|
| Current workflow | Rolls, chemicals, foils, packaging materials, and finished goods are stored, moved, and shipped with ERP or manual records. |
| Pain points | Roll identity, aging, location, partial usage, and quality status can become unclear. |
| Hidden inefficiencies | Searching time, wrong material picks, expired/aged materials, unclear quarantine status. |
| Data sources | ERP inventory, barcode/RFID, roll labels, CoA, warehouse locations, shipping data. |
| AI opportunities | Roll passport, smart search, inventory anomaly alerts, aging-risk prediction. |
| Expected ROI | Medium. |
| Required data | Unique IDs, location, batch, status, usage history. |
| Complexity | Low to medium with barcode discipline. |
| Quick win | Digital roll passport for pilot product family. |
| Long-term | RFID/vision-supported inventory intelligence. |
| Investment | EUR 15k-80k. |
| Business impact | Better traceability and fewer internal errors. |

### Maintenance

| Dimension | Assessment |
|---|---|
| Current workflow | Maintenance likely combines preventive checks, reactive repairs, operator reports, and external service. |
| Pain points | Unexpected downtime, undocumented symptoms, spare-part delays, maintenance knowledge in heads. |
| Lost knowledge | Early warning signs before coating, lamination, drying, winding, or inspection problems. |
| Data sources | Maintenance logs, machine alarms, PLC tags, energy/current/vibration/temperature, operator notes, spare parts. |
| AI opportunities | Maintenance log assistant, anomaly detection, predictive maintenance, spare-part forecasting. |
| Expected ROI | High if critical-line downtime is costly. |
| Required data | Failure history, alarms, operating hours, sensor streams. |
| Complexity | Medium for log assistant; high for predictive maintenance if sensor history is weak. |
| Quick win | Maintenance knowledge base and failure-code standardization. |
| Long-term | Predictive maintenance for bottleneck assets. |
| Investment | EUR 20k-150k. |
| Business impact | Higher uptime and less undocumented know-how loss. |

### Production

| Dimension | Assessment |
|---|---|
| Current workflow | Operators run recipes on coating, finishing, lamination, weaving, cutting, or packaging assets using ERP/work orders, local machine settings, process know-how, and visual inspection. |
| Pain points | Recipe transfer from lab to production, batch variation, environmental effects, operator-dependent adjustments, delayed quality feedback. |
| Hidden inefficiencies | Repeated process drift, over-conservative settings, avoidable scrap, unstructured operator observations. |
| Data sources | Work orders, recipes, line settings, speed, temperatures, tension, coating gap, viscosity, humidity, oven zones, energy, defects, QC tests. |
| AI opportunities | Process intelligence, recipe window advisor, anomaly detection, production copilot, energy optimization, digital twin. |
| Expected ROI | Very high but should be staged carefully. |
| Required data | Roll/order IDs, timestamps, parameter history, quality outcomes. |
| Complexity | Medium for analytics; high for closed-loop control. |
| Quick win | Read-only parameter-to-quality correlation for one line/product family. |
| Long-term | Digital twin and human-approved parameter recommendation. |
| Investment | EUR 50k-300k+ over phases. |
| Business impact | Lower scrap, better repeatability, faster root cause analysis. |

### Laboratory And Quality Control

| Dimension | Assessment |
|---|---|
| Current workflow | Tests include physical measurements, thermal tests, water column, bend, flame, tensile and tear tests, plus external tests and certificates. |
| Pain points | Test results may be stored in PDFs, spreadsheets, instruments, paper, or emails; results are hard to connect to recipes and process conditions. |
| Lost knowledge | Why a test failed, which process setting changed, what workaround was used, which customer accepted which variation. |
| Data sources | Lab reports, test instruments, photos, formulations, batch IDs, customer specs, certificates, external labs. |
| AI opportunities | Digital lab notebook, automated test extraction, COA draft generation, predictive quality, test recommendation. |
| Expected ROI | High for R&D cycle time and quality release speed. |
| Required data | Structured test results linked to material, roll, recipe, process, and customer requirement. |
| Complexity | Medium. |
| Quick win | Extract historical lab reports into structured tables and knowledge graph. |
| Long-term | AI experiment planner and predictive release model. |
| Investment | EUR 30k-180k. |
| Business impact | Faster development, fewer repeated experiments, stronger compliance evidence. |

### Packaging

| Dimension | Assessment |
|---|---|
| Current workflow | Finished or semi-finished material is inspected, categorized, packaged, and released. Prior internal context suggests an inspection system may already exist. |
| Pain points | Inspection data often stays local to the machine; defect labels may not feed back to production or R&D. |
| Hidden inefficiencies | Defect classes are counted but not converted into process learning; operator decisions are not captured as training data. |
| Data sources | Inspection images, defect labels, roll IDs, timestamps, operator decisions, packaging status, QC holds, shipment records. |
| AI opportunities | Defect mining, defect taxonomy, quality forecast, roll quality passport, operator support, feedback loop to production. |
| Expected ROI | Very high if existing inspection data is exportable. |
| Required data | Image/defect export, roll/order linkage, labeling consistency, human override decisions. |
| Complexity | Medium for analytics, high for new CV model deployment. |
| Quick win | Use existing inspection outputs to build defect Pareto and roll-level quality intelligence. |
| Long-term | Vision model improvement, predictive quality, and digital twin feedback. |
| Investment | EUR 25k-120k phase 1; EUR 150k+ for robust production CV expansion. |
| Business impact | Reduces repeated defects and creates visible management proof quickly. |

### Finance

| Dimension | Assessment |
|---|---|
| Current workflow | Costing likely combines material cost, labor, machine time, overhead, scrap, and customer/project assumptions. |
| Pain points | True cost of custom products and quality losses may be hard to see. |
| Hidden inefficiencies | Underpriced custom work, hidden rework cost, weak link between process complexity and quote margin. |
| Data sources | ERP, BOM, production time, scrap/rework, purchase prices, energy, labor, quotes, invoices. |
| AI opportunities | Quote-to-margin analytics, cost variance explanation, quality-cost model, cash/working-capital alerts. |
| Expected ROI | High if quote discipline improves. |
| Required data | Product/job costing, quote history, actual costs, rework. |
| Complexity | Medium. |
| Quick win | Margin leakage dashboard for custom jobs. |
| Long-term | AI quote advisor that flags risk and suggests pricing buffers. |
| Investment | EUR 20k-100k. |
| Business impact | Better profitability, especially in custom development and special products. |

### HR And Training

| Dimension | Assessment |
|---|---|
| Current workflow | Training relies on experienced colleagues, documents, machine manuals, and informal knowledge transfer. |
| Pain points | Expert retirement risk, slow onboarding, uneven operator practice, hard-to-find instructions. |
| Lost knowledge | Troubleshooting steps, "why" behind settings, accepted workarounds. |
| Data sources | SOPs, manuals, training docs, videos, operator notes, incident reports, skill matrix. |
| AI opportunities | Operator onboarding assistant, role-based training plans, skills gap dashboard, knowledge capture interviews. |
| Expected ROI | Medium; strategic value is high because knowledge retention is critical. |
| Required data | SOPs, role definitions, training records, expert interviews. |
| Complexity | Low to medium. |
| Quick win | Internal Q&A assistant for SOPs and machine manuals. |
| Long-term | AI-supported skills matrix and succession planning. |
| Investment | EUR 10k-60k. |
| Business impact | Faster onboarding and less dependency on a few experts. |

### IT

| Dimension | Assessment |
|---|---|
| Current workflow | IT supports ERP, network, data access, security, possibly machine connectivity and local databases. |
| Pain points | AI pilots can become risky if they bypass access control, security, or data governance. |
| Hidden inefficiencies | One-off exports, shadow spreadsheets, unclear ownership of master data. |
| Data sources | ERP, file shares, databases, machines, identity/access systems, backup systems. |
| AI opportunities | Read-only data layer, identity-aware knowledge platform, audit logs, secure MLOps. |
| Expected ROI | Indirect but essential. |
| Required data | System inventory, ownership, access rights, data retention policies. |
| Complexity | Medium. |
| Quick win | Secure pilot data room with read-only exports and named data owners. |
| Long-term | Industrial data platform with governance, graph, vector search, and model lifecycle. |
| Investment | EUR 30k-250k depending on architecture. |
| Business impact | Safe scaling instead of isolated demos. |

### Compliance, Documentation, Safety, And Environment

| Dimension | Assessment |
|---|---|
| Current workflow | Standards, certificates, SDS/MSDS, TDS, customer approvals, safety documents, environmental data, and audits are maintained across teams. |
| Pain points | Documentation burden, risk of outdated claims, manual certificate retrieval, complex standards mapping. |
| Hidden inefficiencies | Time spent finding proof rather than improving products; repeated document assembly for customers and audits. |
| Data sources | Certificates, standards, SDS/MSDS, TDS, audit reports, claims library, customer requirements. |
| AI opportunities | Certificate assistant, standards mapping, automatic document packet generation, safety incident trend analysis, energy/emissions analytics. |
| Expected ROI | Medium; risk reduction is high. |
| Required data | Approved document repository, metadata, expiry dates, standards tags. |
| Complexity | Medium because hallucination must be controlled. |
| Quick win | Source-cited compliance/document search with no unsourced answers. |
| Long-term | Certification automation and regulatory risk monitoring. |
| Investment | EUR 20k-120k. |
| Business impact | Faster audits, fewer documentation errors, stronger customer trust. |

---

## Part 3: R&D Transformation

### Why R&D Is The Strategic Center

The public evidence says both companies win through specialized functional combinations:

- Darmstädter refines glass, aramid, and blended fabrics through coatings, appretures, laminations, and hybrid articles.
- Darmstädter has a development lab that mirrors production equipment at small scale.
- Klevers is an integrated weaving operation that can combine raw fabrics, coatings, and laminations for application-specific textiles.
- Klevers has public R&D activity with RWTH Aachen ITA and ZIM-funded projects in custom weaving and basalt ceramic fibers.

This makes R&D the ideal place to create proprietary AI advantage. Competitors can buy machines. They cannot easily copy a well-structured memory of thousands of experiments, recipes, defects, process windows, customer constraints, certificates, supplier effects, and field results.

### R&D North Star

Build a **Materials Intelligence System** that answers:

- Which substrate, weave, coating, lamination, adhesive, foil, and appreture combination best fits a customer requirement?
- Which historical trials are similar?
- Which experiments failed, and why?
- Which process windows are robust in production?
- Which raw material alternatives are technically plausible?
- Which certificates, standards, and lab tests are required?
- Which supplier or batch risks should be checked before scale-up?
- What is the next experiment that maximizes learning per euro and per week?

### R&D Data Model

The minimum data model should connect:

| Entity | Examples |
|---|---|
| Customer requirement | Temperature, flame class, abrasion, water/oil repellency, UV, flexibility, color, width, weight, certification, application |
| Substrate | E-glass, silica glass, aramid, basalt, carbon, blends, V4A reinforcement, filament/textured/roving |
| Finishing route | Silicone, PU, PVA, PAC, vermiculite, graphite, PTFE, appreture, lamination, hybrid |
| Formulation | Binder, filler, pigment, silicone type, solids, viscosity, additives, supplier batch |
| Process | Line, speed, temperature zones, tension, gap, drying/curing, transfer, side count |
| Quality results | Width, weight, thickness, temperature test, water column, bend, flame, tensile, tear, visual defects |
| Certification | ISO, Module B/D, EN 13501, M1, marine approvals, customer-specific approvals |
| Outcome | Approved, failed, reworked, customer complaint, production issue, repeat order |
| Knowledge | Expert notes, root cause, lesson learned, recommended next step |

### Materials AI Opportunities

| Opportunity | Description | First implementation |
|---|---|---|
| Formulation optimizer | Predict coating performance from formulation, substrate, and process parameters. | Start with structured historical trials and lab tests; use Bayesian optimization after data quality improves. |
| Experiment recommendation | Suggest the next best DOE to reduce uncertainty fastest. | Use an LLM assistant plus statistical DOE templates before full active learning. |
| Raw material substitution | Recommend technically plausible substitutes when supplier, price, or regulatory risk appears. | Build SDS/TDS extraction and similarity search. |
| Application recommender | Map customer jobs-to-be-done to product routes and required tests. | Use knowledge graph and source-cited retrieval. |
| Failure analysis | Identify recurring causes behind delamination, blocking, pinholes, poor adhesion, flame failure, low tear strength, color variation, or stiffness drift. | Link failure reports to recipes, batches, process, and tests. |
| Patent and literature mining | Track new binder systems, flame retardants, PFAS-free repellency, high-temperature coatings, basalt/carbon/glass innovations. | Monthly AI literature brief with human R&D review. |
| Supplier intelligence | Monitor supplier documents, discontinuations, price/risk signals, and new grades. | Supplier-material database with risk flags. |
| Scientific research assistant | Ask technical questions across internal reports, certificates, standards, product PDFs, and literature. | RAG system with strict citations and access control. |
| Physics-informed AI | Combine heat transfer, mass transfer, curing, viscosity, and coating weight physics with historical data. | Start with explainable models for process windows. |
| Digital lab notebook | Capture experiments at source rather than after-the-fact PDFs. | Lightweight structured forms linked to attachments and roll IDs. |

### R&D Quick Wins

1. **R&D Memory Capture Sprint:** interview 5-8 senior experts; convert tacit rules into structured "when/then/because" knowledge.
2. **Historical Experiment Extraction:** ingest lab reports, product PDFs, failed-trial notes, and customer specs; extract substrate, coating, process, test, and outcome.
3. **Specification Assistant:** build a source-cited assistant that answers questions only from approved documents and marks uncertainty.
4. **Material Substitution Watchlist:** choose 20 high-risk or high-cost raw materials and build supplier/alternative intelligence.
5. **DOE Template Library:** create reusable experiment plans for coating weight, curing temperature, line speed, viscosity, adhesion, flame tests, and water/oil repellency.

### R&D Long-Term AI Products

- **Coating formulation copilot:** recommends formulation windows and test plans.
- **Hybrid article generator:** proposes combinations of lamination, coating, appreture, substrate, adhesive, and foil for new customer applications.
- **Certificate-aware product designer:** blocks unsafe claims and proposes required tests.
- **Scale-up predictor:** predicts which lab results are likely to fail during production scale-up.
- **Technical textile knowledge graph:** the central knowledge asset behind sales, R&D, production, and quality.

---

## Part 4: Production Transformation

### Production AI Thesis

Production value comes from repeatability under high variability: substrate variation, coating chemistry, line conditions, environmental conditions, operator adjustments, and customer-specific requirements. AI should first observe and explain, then recommend, and only much later control.

### Production Opportunities

| Opportunity | What it does | Data needed | Complexity | Business value |
|---|---|---|---|---|
| Roll-level traceability | Links each roll to order, recipe, process, QC, defects, shipment. | ERP, line records, inspection, QC, labels. | Medium | Very high |
| Predictive quality | Predicts defect or test-failure risk before final release. | Process parameters and quality outcomes. | Medium-high | Very high |
| Anomaly detection | Flags unusual line behavior or parameter drift. | Time-series machine data. | Medium | High |
| AI scheduling | Suggests sequence to reduce changeovers, cleaning, and delays. | Orders, routings, materials, setup rules. | Medium-high | High |
| Recipe optimization | Finds robust process windows by product family. | Recipe, process, outcome history. | High | Very high |
| Energy optimization | Finds energy waste in ovens, drying, motors, compressed air. | Energy meters, process context. | Medium | Medium-high |
| Operator copilot | Gives context-aware SOPs, troubleshooting, and prior cases. | SOPs, manuals, logs, expert notes. | Low-medium | Medium-high |
| Factory digital twin | Simulates bottlenecks, quality risk, and capacity. | Integrated data model. | High | Strategic |

### Production Pilot Scope

Recommended first scope:

- One coating or finishing line.
- One high-volume or high-pain product family.
- 6-12 months of historical orders, process settings, QC results, defects, rework, and complaints if available.
- No control loop. Read-only analysis only.
- Deliverables: defect Pareto, parameter correlation, roll quality passport, root-cause shortlist, dashboard, and data quality report.

---

## Part 5: Quality Transformation

### Quality AI Thesis

Quality should evolve from inspection and certification into **Quality Intelligence**: prediction, explanation, prevention, and evidence automation.

### Core Quality AI Use Cases

| Use case | Description | Expected impact |
|---|---|---|
| Roll quality passport | One view of order, material, process, tests, defects, release status, certificates. | Faster release and complaint response. |
| Defect prediction | Predicts defect risk from material/process context. | Scrap and rework reduction. |
| Root cause AI | Finds similar historical failures and likely causes. | Faster problem solving. |
| Automated CAPA draft | Drafts corrective action based on evidence and prior cases. | Less admin burden. |
| Complaint prediction | Flags products/customers/orders with elevated complaint risk. | Proactive intervention. |
| Supplier quality prediction | Links supplier lots to quality outcomes. | Better procurement decisions. |
| Certificate automation | Assembles correct certificate/test evidence for customer and audit needs. | Faster documentation. |
| Standards assistant | Maps customer/spec requirements to internal tests and certifications. | Fewer compliance mistakes. |

### Quality Metrics To Track

- First-pass yield by product family.
- Rework rate and rework hours.
- Scrap cost and scrap meters/square meters.
- Defects per 1,000 meters or per roll.
- Customer complaints per shipment/product family.
- Time from complaint to root-cause hypothesis.
- Time to release/COA/certificate package.
- Repeat-defect recurrence rate.

---

## Part 6: Packaging Transformation

### Starting Assumption

Prior internal context suggests an inspection system may already be installed in or near packaging. This must be verified during discovery:

- What system is installed?
- Does it store images, defect labels, timestamps, roll/order IDs, operator decisions?
- Can data be exported read-only?
- Are images linked to process and QC results?
- Are defect classes consistent?
- What do operators still detect manually?

### Packaging AI Projects Beyond Computer Vision

| Project | What it does | Why it matters |
|---|---|---|
| Inspection data audit | Maps all available image, defect, label, timestamp, roll, and operator data. | Establishes whether AI is feasible without new sensors. |
| Defect taxonomy cleanup | Standardizes defect labels and severity. | Prevents bad analytics from noisy labels. |
| Defect Pareto by product/process | Shows which defects drive rework/scrap. | Immediate management visibility. |
| Roll quality passport | Links packaging inspection to order, process, QC, and shipment. | Enables traceability and customer response. |
| Operator decision capture | Records accepted/rejected/overridden defect decisions. | Creates training data and captures tacit judgment. |
| Quality forecast | Predicts whether a roll is likely to pass final release. | Reduces late surprises. |
| Feedback loop to production | Connects defect patterns to upstream process conditions. | Converts inspection into prevention. |
| Packaging digital twin | Simulates defect flow, inspection capacity, and release bottlenecks. | Improves throughput and planning. |
| Defect image retrieval | Finds visually similar defects and prior root causes. | Speeds troubleshooting. |
| Customer evidence packet | Assembles inspection images, QC values, and certificates for disputes. | Protects customer trust. |

### Recommended Packaging Pilot Output

After 12 weeks, management should see:

- Which defect classes matter most.
- Which products or process windows create most defects.
- Whether inspection data is reliable enough for computer vision.
- Which roll/order identifiers are missing.
- A prioritized defect-prevention plan.
- A prototype roll quality passport.

---

## Part 7: AI Knowledge Platform

### Platform Vision

Create a secure, source-cited AI system that makes the company's technical knowledge searchable, connected, and reusable without exposing sensitive IP.

### Knowledge Sources

- Emails and meeting notes.
- ERP records.
- PDFs, TDS, SDS/MSDS, certificates, standards.
- Laboratory reports.
- Specifications and customer requirements.
- Production logs and operator notes.
- Quality reports, CAPA, complaints.
- Supplier documentation.
- Machine manuals.
- Images and videos.
- Historical experiments.

### Architecture

| Layer | Purpose |
|---|---|
| Source connectors | Read-only ingestion from ERP, file shares, inspection databases, lab folders, email exports, and document repositories. |
| Document processing | OCR, table extraction, metadata tagging, language detection, duplicate handling. |
| Structured data layer | Roll/order IDs, material IDs, recipes, parameters, tests, defects, suppliers, customers. |
| Knowledge graph | Connects products, materials, processes, tests, certificates, applications, and outcomes. |
| Vector search/RAG | Finds relevant text, images, and prior cases with citations. |
| Analytics/model layer | Predictive quality, anomaly detection, recommendation, clustering, forecasting. |
| Governance | Role-based access, audit logs, source control, approval workflow, retention policy. |
| User apps | R&D copilot, quality copilot, sales engineer assistant, operator copilot, management dashboard. |

### Critical Design Principles

1. **Source-cited answers only:** every technical answer must show the source document, page, or record.
2. **Read-only first:** first pilots should not write to ERP or control machines.
3. **Human approval:** no AI-generated TDS, certificate, customer response, or process change goes out without human review.
4. **IP protection:** use private deployment or secure EU-hosted services; do not upload sensitive recipes to uncontrolled tools.
5. **Data ownership:** every source has a named owner.
6. **Model evaluation:** test for hallucination, retrieval accuracy, and wrong recommendations before rollout.

### Minimum Viable Knowledge Platform

First 90 days:

- 500-2,000 key documents ingested.
- 30-50 core material/product/process entities in a knowledge graph.
- 5 high-value workflows: R&D search, TDS/certificate search, complaint retrieval, defect case retrieval, supplier document search.
- Access limited to the pilot team.
- No model training on confidential data unless legally and technically approved.

---

## Part 8: Industrial AI Roadmap

### 0-3 Months: Prove Value Without Operational Risk

Primary goal: win management trust.

- Create AI governance and pilot charter.
- Appoint AI champion, executive sponsor, IT owner, quality owner, production owner, R&D owner.
- Run data discovery for ERP, inspection, QC, lab, production, complaints, and document repositories.
- Select one pilot product family/line.
- Build read-only data room.
- Build initial knowledge assistant for approved product/QC/R&D documents.
- Build roll-level quality pilot dashboard.
- Define baseline metrics: scrap, rework, defects, complaint time, release time.

Deliverable: management demo with real company data and a quantified next-step case.

### 3-6 Months: Convert Pilot Into Measurable Improvement

- Link order/roll, process, inspection, QC, and complaint data.
- Standardize defect taxonomy.
- Deliver first root-cause analytics and defect Pareto.
- Capture operator/R&D expert knowledge.
- Produce first predictive quality baseline model.
- Build first CAPA/evidence packet assistant.
- Prepare first funding applications where fit is strong.

Deliverable: documented savings potential and decision to scale.

### 6-12 Months: Build The Data Spine

- Expand from one line/product family to 2-3 high-value areas.
- Implement digital lab notebook for new experiments.
- Start formulation/recipe knowledge graph.
- Add supplier TDS/SDS extraction and material substitution intelligence.
- Integrate energy and maintenance data where available.
- Establish AI review board and MLOps process.

Deliverable: repeatable AI operating model and first cross-site data layer.

### 1-3 Years: Industrial AI Platform

- Predictive quality across major product families.
- AI scheduling and changeover optimization.
- R&D formulation assistant with experiment recommendation.
- Sales/application engineering recommender.
- Complaint prediction and customer risk intelligence.
- Supplier quality and raw-material risk prediction.
- Semi-automated certification evidence assembly.

Deliverable: AI becomes part of daily R&D, quality, production, and sales work.

### 3-5 Years: AI-Enabled Technical Textile Leader

- Digital twin for critical production processes.
- Closed-loop, human-approved recipe parameter recommendations.
- Materials AI system for new coatings, laminations, and hybrid articles.
- Proprietary knowledge graph as strategic asset.
- AI-enabled customer co-development portal.
- Patentable AI-assisted formulations/process windows.
- Potential external AI product/service around technical textile development, if strategically desired.

Deliverable: Darmstädter and Klevers become among Europe's most AI-enabled high-performance technical textile specialists.

---

## Part 9: Funding Opportunities

Funding facts below were checked on 2026-07-02. Exact eligibility and budgets must be revalidated immediately before application.

| Funding source | Fit for D&K | What it can fund | Eligibility | Funding amount / level | Partners | Probability | Application strategy |
|---|---|---|---|---|---|---|---|
| ZIM | Very strong | Industrial R&D, cooperation projects, feasibility studies, innovation networks | SMEs and partners; market-oriented R&D | Varies by project type and company size | University/Fraunhofer/RWTH/ITA, AI vendor | High for R&D formulation, predictive quality, material innovation | Use for R&D-heavy AI/materials project, not simple dashboard. Source: [ZIM](https://www.zim.de/ZIM/Navigation/DE/Home/home.html). |
| Forschungszulage | Very strong | Tax credit for R&D labor/contract research if technical uncertainty exists | Any company with German tax residence | Legal entitlement if approved; expanded by 2026 investment package | Optional research partners | High if project has genuine experimental R&D | Apply for AI formulation/predictive quality R&D work with technical uncertainty. Source: [BSFZ](https://www.bescheinigung-forschungszulage.de/). |
| NRW MID-Digitalisierung | Medium, only for marketable digital product | Development or further development of digital products using AI/ML/data mining/real-time/AR-VR | KMU in NRW | 50% up to EUR 15,000 | External service provider | Medium if framed as marketable product, low for internal-only pilot | Use only if creating a customer-facing or marketable digital product, e.g. technical textile recommendation app. Source: [NRW.BANK MID-Digitalisierung](https://www.nrwbank.de/mid-digitalisierung). |
| NRW MID-Assistent(in) | Strong for hiring | Two-year support for a university graduate to implement innovation | KMU in NRW | Up to EUR 48,000 or EUR 33,000 depending on company conditions | New graduate hire | Medium-high | Hire "AI/Data Engineer for Industrial Quality Intelligence" if eligibility fits. Source: [NRW.BANK MID](https://www.nrwbank.de/mid). |
| NRW MID-Digitale Sicherheit | Medium | Digital security investments | KMU in NRW | 50% up to EUR 15,000 | Security provider | Medium | Use for securing AI/data platform, identity, backup, cyber hardening. Source: [NRW.BANK MID](https://www.nrwbank.de/mid). |
| BAFA EEW | Medium-high for energy projects | Energy/resource efficiency, MSR/sensorics/software, process optimization, transformation plans | Companies with eligible energy/resource measures | Depends on module | Energy consultant, integrator | Medium | Use if AI pilot links to oven/drying/energy/resource savings. Source: [BAFA EEW](https://www.bafa.de/DE/Energie/Energieeffizienz/Energieeffizienz_und_Prozesswaerme/energieeffizienz_und_prozesswaerme_node.html). |
| Eurostars / EUREKA | Strong for international R&D | International SME-led R&D with commercialization | Innovative SMEs with international consortium | National funding rules apply | EU/international SME or research partner | Medium | Use for AI-materials platform with partner in marine/fire protection/composites. Source: [Eurostars](https://www.eurekanetwork.org/programmes-and-calls/eurostars/). |
| Horizon Europe Cluster 4 | Strong but competitive | Advanced manufacturing, digital industry, AI, materials, circularity | Consortia | Project/call dependent | Multi-country consortium | Low-medium | Join consortium rather than lead first. Source: [Horizon Europe](https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-europe_en). |
| EIC Accelerator | Low for internal transformation; high only for spin-out product | Deep-tech market-creating product | Startup/SME, TRL 6-8, disruptive market potential | Grant below EUR 2.5M, investment EUR 1-10M | Usually single SME | Low unless external AI product is created | Consider later only if Industrial AI Platform becomes a marketable product. Source: [EIC Accelerator](https://eic.ec.europa.eu/eic-funding-opportunities/eic-accelerator_en). |
| Fraunhofer/RWTH cooperation | Strong | Applied research, validation, sensorics, AI models, materials testing | Contract or publicly funded project | Depends on route | Fraunhofer IPA/ITWM/IAO, RWTH ITA, universities | High as partner route | Use for credibility and grant leverage. |
| KfW/NRW.BANK innovation loans | Medium | Digitalization and innovation investments | Creditworthiness and bank route | Loan, not grant | House bank | Medium-high | Use for larger platform after pilot proves ROI. |

Funding strategy:

1. Do not wait for funding to start the first discovery pilot. It should be small enough to approve internally.
2. Use the pilot to generate evidence for ZIM/Forschungszulage/NRW applications.
3. Separate internal-process AI from marketable AI product ideas. NRW MID-Digitalisierung in 2026 is not the same as a general internal digitalization grant.
4. Package R&D-heavy projects around technical uncertainty: formulation prediction, scale-up, material substitution, and predictive quality.
5. Use university/Fraunhofer partners for credibility, experimental design, and funding success.

---

## Part 10: Risk Analysis

| Risk | Severity | Why it matters | Mitigation |
|---|---|---|---|
| Poor data linkage | High | AI cannot learn if roll/order/process/QC/defect IDs are disconnected. | Start with data mapping and roll passport before modeling. |
| Overpromising AI | High | Management trust can be lost quickly. | Use read-only pilot with measurable KPIs and clear limits. |
| Hallucinated technical answers | High | Wrong product/certification advice can create safety and legal risk. | Source-cited retrieval, no unsourced answers, human approval. |
| IP leakage | High | Recipes, customer specs, and process windows are strategic assets. | Private deployment, access control, vendor due diligence, no uncontrolled uploads. |
| GDPR and employee monitoring | Medium-high | Operator and email data can contain personal data. | Data minimization, works council/employee communication, role-based access. |
| Cybersecurity | High | AI data connectors can expand attack surface. | Read-only connectors, network segmentation, audit logs, security review. |
| Employee resistance | Medium-high | Operators may fear surveillance or replacement. | Frame as defect prevention and knowledge support; involve operators early. |
| Model brittleness | Medium | Process changes can make models stale. | Monitor drift, retrain, keep human override. |
| Funding dependency | Medium | Waiting for grants can delay momentum. | Start small internally; use grants for scale. |
| Vendor lock-in | Medium | Platform may become expensive or inflexible. | Open architecture, data ownership, export rights. |
| Legal/certification liability | High | AI-generated claims could be wrong. | Approved claims library and compliance sign-off. |

---

## Part 11: Executive Prioritization

Scoring scale: 1 = low, 5 = high. Weighted score emphasizes ROI, time to value, strategic importance, feasibility, and knowledge creation.

| Rank | Project | ROI | Investment ease | Difficulty | Visibility | Strategic | Time to value | Risk | Knowledge creation | Weighted score | Recommendation |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 1 | Coating/Packaging Quality Intelligence pilot | 5 | 4 | 3 | 5 | 5 | 5 | 3 | 5 | 4.7 | Start immediately |
| 2 | Roll-level quality passport | 5 | 4 | 3 | 4 | 5 | 4 | 2 | 5 | 4.6 | Build in pilot |
| 3 | R&D knowledge graph and digital lab memory | 5 | 3 | 3 | 4 | 5 | 4 | 3 | 5 | 4.5 | Start in parallel |
| 4 | Complaint/root-cause assistant | 4 | 4 | 2 | 4 | 4 | 5 | 2 | 4 | 4.3 | Quick win |
| 5 | Certificate/TDS/standards assistant | 4 | 4 | 3 | 4 | 4 | 4 | 3 | 4 | 4.1 | Quick win with guardrails |
| 6 | Supplier/SDS/TDS intelligence | 4 | 3 | 3 | 3 | 4 | 4 | 2 | 4 | 3.9 | Phase 2 |
| 7 | Predictive quality model | 5 | 3 | 4 | 5 | 5 | 3 | 4 | 5 | 3.9 | After data linkage |
| 8 | Operator copilot | 3 | 4 | 2 | 4 | 4 | 4 | 2 | 4 | 3.8 | Pilot after SOP ingestion |
| 9 | Energy optimization | 4 | 3 | 3 | 4 | 4 | 3 | 3 | 3 | 3.6 | Use if energy data exists |
| 10 | AI quote/margin advisor | 5 | 3 | 4 | 4 | 4 | 3 | 3 | 3 | 3.6 | Phase 2/3 |
| 11 | AI scheduling optimizer | 5 | 2 | 5 | 4 | 4 | 2 | 4 | 3 | 3.1 | Later |
| 12 | Closed-loop machine control | 5 | 1 | 5 | 5 | 5 | 1 | 5 | 5 | 2.9 | Do not start first |

Top portfolio for the first year:

1. **Pilot:** Coating/Packaging Quality Intelligence.
2. **Foundation:** Roll-level passport and data linkage.
3. **Knowledge:** R&D/lab/specification knowledge graph.
4. **Trust:** Complaint/root-cause assistant.
5. **Compliance:** Source-cited certificate/TDS assistant.

---

## Part 12: Career Strategy For The Internal AI Champion

Your goal is not to be "the person who uses ChatGPT." Your goal is to become the person management trusts to turn AI into measurable industrial value.

### Positioning

Use this identity:

> "I am building a low-risk, measurable AI transformation path for Darmstädter and Klevers, starting with quality and R&D knowledge, then scaling into production intelligence."

Avoid:

- "I want to do AI."
- "We need a big AI platform."
- "AI will automate everything."
- "I can build a model if you give me data."

### Your First 90 Days

1. Interview production, packaging, quality, R&D, sales, IT, and management.
2. Map real data sources and owners.
3. Define one pilot with a baseline and a financial logic.
4. Build a simple prototype or mock dashboard with real exported data if allowed.
5. Present three options to management: do nothing, small pilot, platform-scale program. Recommend the small pilot.
6. Ask for official mandate: pilot approval, data access, one sponsor, and cross-functional working group.

### Political Strategy

| Stakeholder | What they care about | Your message |
|---|---|---|
| CEO/Managing Director | Competitiveness, risk, growth, cost | "This is a low-risk way to protect know-how and reduce quality cost." |
| Production | Stability, workload, practicality | "We start read-only and help operators solve repeated problems." |
| Quality | Traceability, compliance, complaints | "AI will assemble evidence faster and prevent repeat defects." |
| R&D | Experiments, materials, innovation | "We can stop losing experiment memory and accelerate formulation learning." |
| IT | Security, maintainability | "No shadow AI. We use read-only access, governance, and approved architecture." |
| Finance | ROI and budget | "The first pilot has a bounded budget and measurable KPIs." |
| HR/Works council if relevant | Employee trust | "This is knowledge support and quality improvement, not surveillance." |

### Career Milestones

| Milestone | Title you can earn |
|---|---|
| Pilot approved | AI Transformation Lead for Pilot |
| Pilot proves savings or measurable process insight | Industrial AI Project Lead |
| Cross-functional roadmap accepted | AI Transformation Manager |
| Data/knowledge platform funded | Head of Industrial AI / Digital Innovation |
| AI creates patents, funded projects, or customer-facing innovation | Chief AI Officer candidate / Internal entrepreneur |

### How To Create Career Leverage

- Document every decision and result.
- Build allies in production and quality first; they create credibility.
- Translate AI into scrap, rework, complaints, release time, and customer trust.
- Keep management updated monthly with one page.
- Publish internally, not externally first.
- Attach AI to R&D innovation and patentable process knowledge.
- Use funding applications to position yourself as the person who can bring external money and research partners.

---

## Part 13: Executive Presentation Summary

The companion PowerPoint deck created with this report is designed for executive persuasion. It uses minimal slide text, company-specific evidence, a clear first pilot, roadmap, investment logic, risks, and funding options. Every slide includes speaker notes so you can present confidently.

Recommended board ask:

1. Approve a 12-week read-only AI pilot.
2. Name an executive sponsor.
3. Grant controlled data access for one product family/line.
4. Assign one representative each from R&D, production, quality, packaging, IT, and finance.
5. Approve a bounded pilot budget of approximately EUR 25k-75k, refined after data discovery.

Recommended pilot:

**Coating and Packaging Quality Intelligence Pilot**

Purpose:

- Link order/roll, process, inspection, QC, and complaint evidence.
- Identify top defect drivers and repeated root causes.
- Build roll-level quality passport.
- Create first management dashboard.
- Decide whether predictive quality and computer vision expansion are justified.

Success metrics:

- Data linkage rate across target rolls.
- Top 5 defect drivers identified.
- Time to root-cause hypothesis reduced.
- Rework/scrap reduction opportunity quantified.
- Pilot team agrees on scale-up business case.

---

## Immediate Next Steps

1. Validate data access: ERP, inspection system, QC/lab files, production logs, complaints.
2. Select one pilot product family with enough volume, quality pain, and available data.
3. Create baseline: scrap, rework, defects, complaints, release time, energy if relevant.
4. Hold a 60-minute management alignment meeting using the deck.
5. Launch a 2-week data discovery sprint before committing to the full 12-week pilot.

The company does not need to "become an AI company." It needs to become a technical textile manufacturer whose knowledge, quality, and development speed are AI-enabled. That is a much more credible, defensible, and profitable transformation.

