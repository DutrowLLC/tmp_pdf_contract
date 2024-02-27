

contract_obj = {
    'contract_type': 'AGREEMENT', # Can be 'AGREEMENT', or 'PROPOSAL'

    'document_number' : '12345',  # This goes in the footer of each page

    # COMPANY INFO
    'company_address_line1': '8466 Tyco Rd Ste B',
    'company_address_line2': 'Vienna, VA 22182',
    'company_phone_number':  '(703) 951-6911',

    # CUSTOMER INFO
    'customer_first_name':      'Jane',
    'customer_last_name':       'Smith',
    'customer_email':           'janesmith@gmail.com',
    'customer_phone':           '(123) 456-7890',
    'customer_address_line1':   '1234 Camden St',
    'customer_address_line2':   'Alexandria, VA 22308',

    # CDAA REPRESENTATIVE
    'rep_first_name':  'Jim',
    'rep_last_name':   'Jenson',
    'rep_email':       'jimjenson@cdaainc.com',

    # ACKNOWLEDGEMENT (Only in "AGREEMENT", not in "PROPOSAL")
    'acknowledgement': "Upon acceptance of this Agreement by CDAA, CDAA agrees to perform the work at the price shown below and thecustomer agrees to allow CDAA to perform the approved work and to pay CDAA the Total Agreement Amount. All direct costs, supplements, overhead and profit are included in the Total Agreement Amount and are due to CDAA in accordance with the payment schedule below. Any upgrade(s) or additional work requested by the customer will only be performed after the execution of a written change order by CDAA and the Customer(s).",

    # JOB SCOPE SECTION
    'job_scope': {
        'home_image_file_path': '../roof/home_image.jpg',
        'introduction': """Removal and disposal of current shingles and roofing materials. Replacement of 29 squares of all roof-
ing materials listed below using and installed in compliance with 50 year grade shingles. No gutters

or downspouts replacements. Any rotten or damaged decking will be replaced with new, up to 3
sheets only, additional sheets will be covered at revised cost.
""",
        'bullet_points': [
            "Remove 29 squares of all existing shingles down to deck.",
"""Renail any loose wood. If bad or rotten wood is discovered
* 3 SHEET IS INCLUDED *
""",
"Install 29 squares of GAF HDZ Shingles, TBD color.",
"Install 3 bundles of GAF Cap Ridge Shingles.",
"Install 30 pieces of 10 ft drip edges.",
"Install 180LF of step flashing and a row flashing.",
"Install 3 bundle of GAF ProStart Starter Strip Shingles",
"Install new ridge vents",
"Install Green Cap Coil Nails Weather-proof to prevent leaks and high winduplifts.",
"Install 3 rolls of GAF Deck Armour Underlayment to keep roof dry.",
"Install 6 rolls of GAF StormGuard Ice at all gutter lines, rake edges and valleys.",
"Install 3 new pipe flashings",
"Install 2 boxes of roofing nails.",
"Install 3 silicone tubes to seal the roof.",
"Create 2 new 22 x 46 openings in theroof",
"Install 2 new 22x 46 skylights",
"Create 2 new framings to mount the skylights",
"Open the drywall from the room ceiling to the roof, going through the attic space. Depending on the size of the attic drywall work might vary, it can go down or up. Calculates on average size attic.",
"Finish interior drywall associated",
"Install necessary exterior flashing to make skylight water tight.",
"Clean up all job related debris"
        ]

    },

    # MATERIALS SECTION
    'materials': {
        'materials_images_file_path': '../assets/',
        'materials_list': [
            {
                'name': 'GAF Shingles Timberline HDZ Color TBD',
                'description': """Timberline HDZ - The right combination of beauty, performance and reliability in a genuine woodshake look.""",
                'image_file_path': 'gaf_timberline_hdz.jpg',
                "quantity": 29,
                "price_each": 234.0,
                "total_price": 6786.0
            },
            {
                'name': 'Roofing Warranty System Plus Warranty',
                'description': 'During the Smart Choice® Protection Period: GAF will pay you the full reasonable cost of labor to repair or re-cover any defective GAF Product(s) (excluding non-GAF accessories, metal work, or flashing) and will provide replacement GAF Products or the reasonable cost of obtaining replacement GAF Products, at GAF’s option. The cost of labor to tear off some or all of your GAF Products is included if necessary to repair your roof. GAF will not pay costs to dispose of any roof products',
                'image_file_name': 'roofing_warranty_system.png',
                'quantity': 1,
                'price_each': 80.0,
                'total_price': 80.0
            },
            {
                'name': 'Cap Ridge Shingles',
                'description': 'They are specially designed to cover the ridges of the roof, which are high-stress areas that need more protection. The difference is they are thicker and pre-bent to allow them to fit along the ridge easily',
                'image_file_name': 'ridge_cap_shingles.jpg',
                'quantity': 3,
                'price_each': 114.0,
                'total_price': 342.0
            },
            {
                'name': 'Drip Edge',
                'description': 'Drip edges are metal sheets, usually shaped like an “L,” installed at the edge of the roof. Also called drip edge flashing or D-metal, they serve a vital function by directing water away from the fascia and into the gutter and avoid from getting underneath your roofing.',
                'image_file_name': 'drip_edge.jpg',
                'quantity':30,
                'price_each': 13.50,
                'total_price': 405.0
            },
            {
                'name': 'Step Flashing',
                'description': 'Step flashing is a piece of metal, bent at 90 degrees, that goes between the shingles and a sidewall, dormer, or chimney. It prevents water from getting under the shingles and destroying the roof structure by directing it back to the shingles below and off the roof',
                'image_file_name': 'step_flashing.png',
                'quantity': 1,
                'price_each': 218.50,
                'total_price': 218.50
            },
            {
                'name': 'Row Flashing + Chimney flashing',
                'description': 'Row flashing is a thin material, usually galvanized steel, that professional roofers use to direct water away from critical areas of the roof, wherever the roof plane meets a vertical surface like a wall or a dormer. Flashing is installed to surround roof features, such as vents, chimneys, and skylights.',
                'image_file_name': 'chimney_flashings.jpg',
                'quantity': 1,
                'price_each': 200.0,
                'total_price': 200.0
            },
            {
                'name': 'Starter strip',
                'description': """Shingle strips applied along the downslope eave line before the first course of roofing and intended to fill spaces between cut-outs and joints of the first course. They aid the roof's water-shedding function by covering shingle joints and cutouts""",
                'image_file_name': 'starter_strip.jpg',
                'quantity': 3,
                'price_each': 114.0,
                'total_price': 342.0
            },
            {
                'name': 'Ridge Vent',
                'description': """Air exhaust vent installed on the peak of a roof which allows warm, humid air to escape a building's attic.""",
                'image_file_name': 'gaf_vent_feature.jpg',
                'quantity': 27,
                'price_each': 27.0,
                'total_price': 729.0
            },
            {
                'name': 'GAF Deck Armour Underlayment',
                'description': 'It covers your entire roof deck, acting as a secondary moisture barrier between the roof deck and the overlying shingles (or other roof covering) to help prevent wind-driven rain from infiltrating your home through the roof. In other words.Made from varying blends of cellulose (natural plant fibers), polyester, bitumen or asphalt. Typically, this underlayment has a basemat, or a flexible base layer, saturated with asphalt for water resistance. In other words, it helps keep your home dry',
                'image_file_name': 'gaf_roofing_system.jpg',
                'quantity': 4,
                'price_each': 171.0,
                'total_price': 684.0
            },
            {
                'name': 'GAF Storm Guard Ice and Shield',
                'description': 'GAF StormGuard Film-Surfaced Leak Barrier will create a seal that helps keep water out at the most vulnerable areas of your shingle or metal roof (at the eaves and rakes, in valleys, around chimneys, etc.). Help protect your home from the costly wall and ceiling staining. Keeps damage caused by ice dams and wind-driven rain away.',
                'image_file_name': 'gaf_storm_guard_ice_and_shield.jpeg',
                'quantity': 6,
                'price_each': 130.0,
                'total_price': 780.0
            },
            {
                'name': 'Roof Pipe Flashing',
                'description': 'Manufactured to seal tightly around small ventilation pipes, plumbing, and other vents and equipment that protrude from the roof of a home or commercial building. The base is typically a flexible metal so that it is compatible with virtually any roofing material.',
                'image_file_name': 'roof_pipe_flashing.jpg',
                'quantity': 3,
                'price_each': 15.50,
                'total_price': 46.50
            },
            {
                'name': 'Roof Vents',
                'description': 'Roof vents form the base of your attic ventilation system. They let your attic breathe—and they help protect your roof system from damaging heat and moisture',
                'image_file_name': 'roof_vents.jpg',
                'quantity': 1,
                'price_each': 36.0,
                'total_price': 36.0
            },
            {
                'name': 'Nails',
                'description': 'The main feature that distinguishes a roofing nail is its large head, which is usually much larger and flatter than other types of nails. This permits the nail to hold down roofing shingles without tearing through the material.',
                'image_file_name': 'nails.jpg',
                'quantity': 2,
                'price_each': 114.0,
                'total_price': 228.0
            },
            {
                'name': 'Silicone tubes',
                'description': 'A high solids non-shrinking moisture-cure silicone sealant intended for sealing and repairing roofs, Minimal odor, contains no solvents and is used to seal penetrations and terminations. Excellent adhesion to concrete, masonry and wood.',
                'image_file_name': 'silicon_tubes.jpg',
                'quantity': 3,
                'price_each': 13.50,
                'total_price': 40.50
            },
            {
                'name': 'Plywood',
                'description': 'CDX 1/2 inch 4x8 is a type of veneer plywood that is fabricated by gluing and then pressing sheets of wood together to strengthen them. The grains run in the opposite direction of the layer below. Known for their strong resistance to cracking, breaking, or twisting',
                'image_file_name': 'plywood.jpeg',
                'quantity': 1,
                'price_each': 0,
                'total_price': 0
            },
            {
                'name': 'Green Cap Coil Nails Weatherproof',
                'description': 'Cap nails are used to attach roofing felt, house wrap, and tar paper to prevent leaks or high wind uplifts. Unlike galvanized nails, a cap nail has a steel shank and a large polyethylene cap to prevent leaks, and rusting and assure a greater holding power. Cap nails are typically used for fastening felt underlayment and not asphalt shingles.',
                'image_file_name': 'green_cap_coil_nails_weatherproof.jpg',
                'quantity': 1,
                'price_each': 118.0,
                'total_price': 118.0
            },
            {
                'name': 'Labor',
                'description': 'Is responsible for performing various tasks to aid daily operations at a construction site. Their duties include loading and unloading tools or raw materials, and assembling roof elements or other pieces of equipment that will result in the completion of the roof replacement process.',
                'image_file_name': 'labor.jpeg',
                'quantity': 29,
                'price_each': 119.0,
                'total_price': 3451.0
            },
            {
                'name': 'FLAT RUBBER ROOF',
                'description': 'INCLUDES ALL MATERIALS NEEDED FOR THIS ROOF; - Black EPDM rubber membrane -Adhesive - Primer -Metal flashing between both roofs shingle/rubber - Flashing tape - Drip edge for flat roofs',
                'image_file_name': 'flat_rubber_roof.jpg',
                'quantity': 1,
                'price_each': 4000.0,
                'total_price': 4000.0
            },
            {
                'name': 'VELUX 22x46 Tempered Glass',
                'description': 'Fixed skylight. The No Leak Promise is our commitment that VELUX Skylights installed with our flashing will not leak. We’re able to make this commitment with a 10-year installation warranty backed by our patented three layers of water protection on deck- and curb-mounted skylights.',
                'image_file_name': 'tempered_glass.jpg',
                'quantity': 2,
                'price_each': 350.0,
                'total_price': 700.0
            },
            {
                'name': 'VELUX FLASHING KIT',
                'description': 'Made specifically for skylight sizes to achieve a water-tight area around the shingles',
                'image_file_name': 'velux_flashing_kit.jpeg',
                'quantity': 2,
                'price_each': 150.0,
                'total_price': 300.0
            },


            {
                'name': 'LABOR SKYLIGHTS INSTALLATION EXTERIOR',
                'description': 'Certified and licensed crew to install framing and installing skylight on roof.',
                'image_file_name': 'man_in_red_shirt_screws_a_skylight_to_a_roof.png',
                'quantity': 2,
                'price_each': 400.0,
                'total_price': 800.0
            },
            {
                'name': 'DRYWALL WORK',
                'description': """- Open ceiling area to roof area going through attic
                -Includes FRAMING
                - drywall
                - plaster
                - sanding
                - prime
                - paint to match the area installed
                **Included**
                Our comprehensive service encompasses a preparation and clean-up procedure cost, which incorporates the implementation of a ZIP wall dust barrier protection system. This system ensures a meticulously screened environment, safeguarding both the room and floor from any potential damage or dirt accumulation during various tasks such as painting, sanding, and drywall fixings. The utilization of this protective measure not only upholds the integrity of the immediate work area but also prevents any adverse impact on the surrounding areas of the residence.""",
                'image_file_name': 'drywall_work.jpg',
                'quantity': 2,
                'price_each': 2000.0,
                'total_price': 4000.0
            }
        ]
    },

    # TERMS OF AGREEMENT
    'terms_of_agreement': [
        {
            'heading': "Acceptance",
            'text':"""All approved scopes and supplements are incorporated into this Agreement as if stated in full.No work will be performed or material furnished except as specified herein or agreed to in writing. Any modifications to this contract which changes the cost, materials, or work to be performed or estimated completion date must be in writing and signed by all parties. A change order shall be executed by both parties stating the terms of the change, the additional cost or deduction, and the additional time. Extra Work shall increase Total Agreement Amount and time stated herein. All CDAA's rights and remedies under this Agreement extend to change orders and Extra Work. Unless otherwise agreed in writing all changes are at CDAA's regular price. This contract does not include, unless expressly specified, any asbestos abatement, removal or encapsulation, or any removal of lead paint. If asbestos or lead paint is found existing on the premises, the cost to abate, remove, or encapsulate shall be paid by Owner as extra. Thiscontract does not include, unless expressly specified, any wood replacement, repair or insulation. Owner represents that Owner owns the property on which work is to be performed. The contractor shall comply with all local requirements for building permits, inspections, and zoning. All surplus material remains CDAA's property. During work CDAA may use Owner's utilities, and all charges shall be Owner's responsibility. If CDAA is unable to complete work for any reason. It may assign or subcontract its obligations hereunder to a contractor of its choice. Owneragrees to execute all other documents which CDAA may require in order to carry out the terms of this Agreement or comply with all applicable laws. CDAA may make minor variations in work or substitute material of equal or better quality without consent of the Owner."""
        },
        {
            'heading': "Temporary Power, Utilities",
            'text': """Pursuant to the agreement herein, the Owner consents to furnish essential utilities, including but not limited to water and electricity, required for CDAA personnel to efficiently undertake and complete the Project. Owner agrees to grant access to the property's bathroom facilities. It should be noted that CDAA employees, in compliance with OSHA regulations, will be fully attired in professional work gear which may include suits and boots. As an inherent consequence of their duties, this attire may incidentally carry fragments of removed insulation/debris or induce a unique odor during the insulation application process, potentially affecting the air quality within the bathroom and surrounding areas. Despite precautions to minimize these occurrences, the bathroom facilities might be subject to incidental splashes and drips that are an inevitable part of the job, possibly necessitating a comprehensive post-use cleaning. Recognizing the potential inconvenience this may cause, CDAA highly recommends the deployment of a dedicated job site portable toilet. This service is available at a standard rate of $500 and aims to preserve the integrity of the Owner's interior spaces while mitigating disruption. The Owner's consideration of this recommendation is greatly appreciated as we strive for the highest level of professionalism and convenience throughout the project"""
        },
        {
            'heading': "Skylights",
            'text': """Old skylights on the roof are typically constructed using clear thermoplastic or regular glass (not tempered), materials that are no longer commonly used in modern skylights due to their fragility. These materials are susceptible to cracking or breaking as a result of construction vibrations caused by demolition, nailing, and walking on the roof. In such events, CDAA will not be held liable and will be relieved of responsibility for restoring the area to its pre-construction conditions. CDAA does not bear responsibility for any occurrences of drywall cracking and deterioration around skylights inside the property when the skylights are being replaced or reset. The homeowner is solely accountable for all interior drywall work."""
        },
        {
            'heading': "Area Cleaning",
            'text': """CDAA's cleaning responsibilities are limited to the immediate area surrounding the structure where the roofing job took place. The debris removal process entails the removal of larger debris, such as discarded roofing materials, nails, and equipment or tools used during the installation. To ensure thorough removal of nails and metal debris, CDAA utilizes a magnetic nail finder. Meticulous sweeping with a broom is conducted, with attention given to corners, edges, and hard-to-reach spaces. Additionally, blowers are utilized effectively to eliminate fine particles, dust, and debris from the surface and difficult-to-access areas, including gaps between structures or roofing elements. CDAA's focus remains on cleaning up debris and materials within the defined area. It should be noted that CDAA cannot be held responsible for debris picked up and dispersed by wind or debris that travels beyond the immediate area surrounding the structure. The Owner acknowledges that the movement of debris caused by natural elements, such as wind, is beyond CDAA's control. Consequently, the Owner assumes responsibility for any debris or materials that may travel to neighboring properties or areas beyond the immediate vicinity of the structure. The Owner agrees to promptly address and clean up any debris that extends beyond the limited cleaning area to ensure that neighboring territories are not affected."""
        },
        {
            'heading': "Grass, Driveway Parking",
            'text': """Owner agrees to provide a nearby parking space for the purpose of accommodating our spray foam rigs. Given the limitations on hose length, it is critical that these rigs, whether they are housed in a trailer or a heavy-duty box truck, have sufficient parking space near the house. There may be occasions where we need to park in restricted areas to complete our work. As a result, any parking fines or tickets received due to parking the rigs in such areas will be considered as a necessary project expense and will thus be transferred to the client. Additionally, the use of trailers or trucks may result in tracks and indentations in the soil, as well as oil drops, marks, and scuffs on driveways caused by work vehicles. CDAA will not be held liable and will be relieved of responsibility for restoring the area to its pre-construction conditions in such events. While efforts will be made to preserve the area surrounding the structure, certain impacts may occur, including stamping, breaking, or damage to grass, shrubs, and trees due to foot traffic, falling debris, and material placement. Additionally, the use of dump trailers or trucks may result in tracks and indent ations in the soil, as well as oil drops, marks, and scuffs on driveways caused by work vehicles. CDAA will not be held liable and will be relieved of responsibility for restoring the area to its pre-construction conditions in such events."""
        },
        {
            "heading": "Cancellation",
            "text": """This contract creates a mortgage or lean against the property to secure payment and may cause a loss of your property if you fail to pay the amount agreed upon. You have the right to rescind this contract within 3 business days after the date you sign it by notifying the contractor in writing that you are rescinding the contract. Owner acknowledges that all materials listed, or any change orders (''Materials") are specially ordered and may not be canceled by the Owner after the Rescission period has expired without a cost. If Owner wishes to cancel the contract after 3 business days but prior to the start of the project, CDAA will return the deposit with less cost of materials ordered and less $1000 non-refundable deposit fee. If Owner cancels the Agreement after the Rescission period and work has begun or Materials have been ordered, the Owner shall pay, upon giving notice that Owner is canceling this Agreement, to CDAA the total amount of any and all work started or completed up to the point of cancellation, including cost of Materials, and twenty-five percent (25%) of the remaining Total Agreement Amount as liquidated damages plus any termination expenses incurred by CDAA including but not limited to canceling orders and subcontracting agreements. If Owner cancels the Agreement after the Rescission period and work has not begun nor Materials ordered, the Owner shall pay to CDAA twenty-five percent (25%) of the Total Agreement Amount as liquidated damages plus any termination expenses incurred by CDAA including but not limited to canceling orders and subcontracting agreements."""
        },
        {
            "heading": "Default",
            "text:":"""The Owner shall be in default under this Agreement in the event that any of the following conditions or events occur: (a) Owner fails to pay any payments, in full, under the Payment Schedule: (b) Owner fails, within 5 days from the date CDAA contacted Owner to schedule the work, to contact CDAA and schedule the work: ( c) Owner fails to provide full access to CDAA between the hours of 7:30 am. to 6:00 pm., Monday through Saturday to perform the work described herein: or (d) any other failure of Owner to fully and completely comply with the terms and conditions of this Agreement. Owner acknowledges that CDAA has title to the Materials used in performing the work described herein. Owner agrees that title to the Materials does not pass to Owner under this Agreement until the Total Agreement Amount is paid in full. Owner further agrees and acknowledges that in the event of default. CDAA has a greater right to possession of the Materials than does Owner and further agrees to grant CDAA access to recover the Materials within ten (10) days after being notified by CDAA of the default. If Owner defaults and CDAA has completed all the work, Owner shall pay CDAA the Total Agreement Amount. If Owner is in default and work has begun or Materials been ordered, Owner shall pay, within 5 days from the date that CDAA notifies the Owner that Owner is in default to CDAA the total amount of any and all work started or completed, including the cost of the Materials, and twenty-five percent (25%) of the remaining Total Agreement Amount as liquidated damages plus any termination expenses incurred by CDAA including but not limited to canceling orders and subcontracting agreements. If Owner fails to pay the amounts owed in accordance with this Agreement CDAA shall pursue legal action. If CDAA pursues any legal action to enforce any provision or obligation of this Agreement then CDAA shall be entitled, in addition to its damages, all of CDAA's expenses, including CDAA's reasonable attorney's fees, expert witness fees, and costs, incurred in pursuing any amount owed under this Agreement or seeking to enforce this Agreement in any way. If Owner is in default, starting on the date of default, Owner agrees that CDAA shall charge interest on any amount due at a rate of five (5%) percent per month (month over month) with a minimum charge of $200.00 per month. Consent is hereby given for filing of mechanic's liens by any person who supplies materials or services for the work described in this contract on the property on which it is located if he is not paid."""
        },
        {
            "heading": "Workmanship Warranty",
            "text:":"""This Roof Warranty is being provided by CDAA Inc., hereinafter referred to as the "Warrantor," to the original purchaser, hereinafter referred to as the "Owner," in relation to a newly installed roof on the property located at the address specified in the associated contract. This Warranty is valid for a period of twelve (12) months from the completion date of the roof installation. This Warranty applies solely to defects that arise under normal use and maintenance of the roof.

Warranty Claims: In order to initiate a warranty claim, the Owner must provide written notice to the Warrantor within thirty (30) days of discovering any alleged defect. The written notice should include a detailed description of the defect, accompanied by supporting documentation and photographs, if available. The Warrantor shall be afforded a reasonable opportunity to inspect the alleged defect prior to proceeding with any repairs or replacements covered by this Warranty. Remedies: The Warrantor reserves the right to choose the appropriate remedy based on the nature and extent of the defect. If the Warrantor identifies and verifies the existence of a covered defect, it shall, at its sole discretion, elect to: 1) Rectify workmanship defect by replacing or repairing the affected roof materials. 2) Substitute the defective portion of the roof installation with new materials and workmanship of similar quality. Exclusions: This Warranty does not cover defects or damages resulting from: 1) Improper maintenance, or repairs performed by parties other than the Warrantor. 2) Negligence, misuse, or abuse by the Owner or any third party. 3) Acts of nature, including, but not limited to, fire, flood, windstorm, earthquake, lightning, or hail. 4) Alterations, modifications, or additions made to the roof installation without the prior written consent of the Warrantor. Any repairs or replacements performed under this Warranty shall not extend the original twelve (12) month warranty period."""
        },
        {
            "heading": "Hidden and Pre-Existing Conditions",
            "text:":"""Owner(s) will be notified of any hidden conditions found by CDAA during the performance of work as described herein, including conditions that may constitute code violations. Additional charges due to these conditions will be submitted to the Owner for the Extra Work in written form as a change order. CDAA is not responsible for pre-existing construction deficiencies that manifest themselves during the construction process: i.e., nail pops, wood rot, decking deflection, soft or hard soil conditions, upgrades required by codes or regulations, removal of an additional (2nd and 3rd) layers of existing roof, etc. If a construction problem is pointed out prior to construction and CDAA is notified in writing, CDAA will try to assist Owner to correct the problem(s) on a time and material basis. Owner releases CDAA from any damage that is incurred during the work to hidden components, including but not limited to pipes, electrical wiring, or any other hidden component."""
        },
        {
            "heading": "Limitations",
            "text:":"""CDAA shall have no responsibility for damages from rain, fire, tornado, windstorm or other perils, as is normally contemplated to be covered by Homeowners Insurance or unless specified written agreement has been made therefore prior to commencement of work. During the duration of the work the Owner shall notify its homeowners insurance of the construction and will purchase coverage necessary for any interior damage or other construction related damage. CDAA will put all efforts in place for a damage(s) commencement of the project, however any damages caused to the interior of the property and/or Owners belongings during the construction and in the result of the construction will not be covered by CDAA unless specified written agreement has been made therefore prior to commencement of work. Replacement of deteriorated decking, fascia boards, roof jack, ventilator, flashing or other materials, unless otherwise stated in this Agreement are not included and will be charged as an extra on a time and materials basis. CDAA shall not be responsible for slight scratching or denting of gutters, oil droplets in driveways, hairline fractures in concrete or driveway, sinking or crumbling in concrete or driveway, or damage to plants and shrubbery. If excessive damage is caused by CDAA, in CDAA's sole and absolute discretion, CDAA will repair or replace the damaged area only. CDAA will provide only standard foundations (if applicable) and any additional earthwork, foundations of earth movement, including differing site conditions, shall be outside the scope of the Agreement and will be performed by CDAA only as Extra Work. Owner waives any and all claims for consequential, punitive, special incidental, and indirect damages for any claim brought by Owner against CDAA. CDAA's maximum liability for any claim relating to this Agreement, whether in tort, contract or otherwise shall be limited to 25% of the Total Agreement Amount. Owner shall notify CDAA, in writing, of any defect in workmanship or Materials within 24 hours after discovering the defect. Oral notification of a defect is ineffective. CDAA shall have 30 business days to cure the defect. No claim or defense shall be brought by Owner until CDAA has had the opportunity to cure the defect. If Owner fails to provide timely notice to CDAA of the defect and an opportunity to cure. Owner waives any right to recover damages for the defect and shall be barred from bringing a cause of action, or defense in any action brought against Owner. Emergency Wind Damage Repairs are performed to mitigate, but not eliminate, potential damage. The emergency repair is not a full repair. Owner acknowledges and agrees that the Emergency Wind Damage Repair is temporary, and that damage can still occur despite the emergency repair. CDAA cannot guarantee that the Emergency Wind Damage Repair will prevent any water or further damage to Owner's home. Therefore, as a condition to performing the Emergency Wind Damage Repair. Owner releases CDAA from any and all damage and liability, including but not limited to, water damage that may occur after the Emergency Wind Damage Repair has been made. The Emergency Wind Damage Repair carries no warranty, of any type."""
        },
        {
            "heading": "Performance and Delays",
            "text:":"""No Materials will be delivered to Owner until after the Rescission period has expired. Installation of Materials will not begin until such time CDAA receives the second payment from Owner. CDAA has the right to reschedule the project due to, but not limited to; weather conditions, materials delivery delays, ongoing project delays, etc.

THE APPROXIMATE COMMENCEMENT AND COMPLETION DATES OF THIS AGREEMENT ARE ONLY ESTIMATES AND CDAA SHALL NOT BE RESPONSIBLE FOR DELAYS IN EITHER THE STARTING DATE FOR THE WORK OR THE SUBSTANTIAL."""
        },
        {
            "heading": "Completion Date as Listed Herein",
            "text:":"""CDAA shall not be held responsible for delays or failures arising from causes beyond its control, including but not limited to acts of God, natural disasters, epidemics, labor disputes, transportation disruptions, power outages, technology failures, severe weather, and actions of third parties. Such delays caused by these events shall not be considered as abandonment and shall not be factored into payment or performance timelines. The Owner acknowledges and agrees that any claims for damages related to such delays are waived. Furthermore, the Owner confirms that the agreed commencement and Substantial Completion dates in this Agreement were not relied upon and did not form the basis of the agreement between the parties. Owner agrees to provide final payment upon Substantial Completion of the Project as described in the Payment Schedule. It shall be deemed "Substantially Completed" when the homeowner takes possession of Materials and is able to occupy the dwelling. Upon Substantial Completion. Owner releases CDAA from any and all liability, cause of action or claim under this Agreement, except the punch list work and the Labor Warranty. In the event that any provision of this Agreement is invalidated by a court of competent jurisdiction, then all of the remaining provisions of this Agreement shall continue unabated and in full force and effect. This Agreement contains the entire agreement between the parties. This Agreement supersedes all other written or oral agreements. Section headings are for convenience only and shall not affect the construction of any provision of this Agreement. The Agreement shall be deemed jointly drafted by the parties and any ambiguity shall not be interpreted against either party. Owner agrees that upon acceptance of this Agreement by CDAA, each Owner shall be jointly and severally liable for any amounts owed pursuant to this Agreement. When multiple Owners have executed this Agreement, each of the Owners hereby agrees that each of the Owners is an agent for the other Owners and each Owner may act on behalf of the other Owners for the purposes of making specification changes, work order changes, executing change orders and modifications to this Agreement."""
        },
    ],

    "pay_schedule": {
        "pay_schedule_list": [
            {
                'description': "Down Payment Due upon execution of this Agreement (33%)",
                'amount': "$7,920.00"
            },
            {
                'description': "Second Payment Due Upon Delivery of Material (33%)",
                'amount': "$7,920.00"
            },
            {
                'description': "Balance Due Upon Substantial Completion (34%)",
                'amount': "$7,920.00"
            }
        ],
        'total_contract_amount': '$24,000.00'
    },



}

