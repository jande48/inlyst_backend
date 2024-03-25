def capitalize_first_letter(words):
    try:
        words_split = words.split(" ")
        return " ".join(elem.capitalize() for elem in words_split)
    except:
        return words


def populate_property_object(p, pa):
    try:
        p.property_type = pa["propType"]
    except:
        p.property_type = None
    try:
        p.building_type = pa["buildgType"]["value"]
    except:
        p.building_type = None
    try:
        p.square_footage = int(float(pa["buildgSqFt"]))
    except:
        p.square_footage = None
    try:
        p.living_square_footage = int(float(pa["livingSqFt"]))
    except:
        p.living_square_footage = None
    try:
        p.property_square_footage = int(float(pa["propSqFt"]))
    except:
        p.property_square_footage = None
    try:
        p.parking_square_footage = int(float(pa["parkingSqFt"]))
    except:
        p.parking_square_footage = None
    try:
        p.property_acres = pa["propAcres"]
    except:
        p.property_acres = None
    try:
        p.land_use = capitalize_first_letter(pa["landUse"]["value"])
    except:
        p.land_use = None
    try:
        p.roof_cover_type = pa["roofCoverType"]["value"]
    except:
        p.roof_cover_type = None
    try:
        p.subdivision_name = capitalize_first_letter(pa["subdivision"])
    except:
        p.subdivision_name = None
    try:
        p.built_year = pa["builtYear"]
    except:
        p.built_year = None
    try:
        p.effective_built_year = pa["effectiveBuiltYear"]
    except:
        p.effective_built_year = None
    try:
        p.bedrooms = pa["bedrooms"]
    except:
        p.bedrooms = None
    try:
        p.baths = pa["baths"]
    except:
        p.baths = None
    try:
        p.partial_baths = pa["partialBaths"]
    except:
        p.partial_baths = None
    try:
        p.mobile_home = pa["mobileHome"] == "Y"
    except:
        p.mobile_home = None
    try:
        p.cooling_type = pa["coolingType"]["value"]
    except:
        p.cooling_type = None
    try:
        p.assessed_value = pa["assessedValue"]
    except:
        p.assessed_value = None
    try:
        p.market_value = pa["marketValue"]
    except:
        p.market_value = None
    try:
        p.appraised_value = pa["appraisedValue"]
    except:
        p.appraised_value = None
    try:
        p.tax_amount = pa["taxAmount"]
    except:
        p.tax_amount = None
    try:
        p.sales_date = pa["salesDate"]
    except:
        p.sales_date = None
    try:
        p.prior_sales_date = pa["priorSaleDate"]
    except:
        p.prior_sales_date = None
    try:
        p.foundation = pa["foundation"]["value"]
    except:
        p.foundation = None
    try:
        p.tax_address = capitalize_first_letter(pa["taxAddress"])
    except:
        p.tax_address = None
    try:
        p.main_address_line = capitalize_first_letter(
            pa["formattedTaxAddress"]["mainAddressLine"]
        )
    except:
        p.main_address_line = None
    try:
        p.address_number = pa["formattedTaxAddress"]["addressNumber"]
    except:
        p.address_number = None
    try:
        p.street_name = capitalize_first_letter(pa["formattedTaxAddress"]["streetName"])
    except:
        p.street_name = None
    try:
        p.street_type = pa["formattedTaxAddress"]["streetType"]
    except:
        p.street_type = None
    try:
        p.city = capitalize_first_letter(pa["formattedTaxAddress"]["city"])
    except:
        p.city = None
    try:
        p.state = pa["formattedTaxAddress"]["state"]
    except:
        p.state = None
    try:
        p.post_code_1 = pa["formattedTaxAddress"]["postCode2"]
    except:
        p.post_code_1 = None
    try:
        p.post_code_2 = pa["formattedTaxAddress"]["postCode1"]
    except:
        p.post_code_2 = None
    try:
        p.owner_first_name = pa["owners"][0]["firstName"]
    except:
        p.owner_first_name = None
    try:
        p.vacancy = pa["vacancy"]["value"]
    except:
        p.vacancy = None
    try:
        p.owner_middle_name = pa["owners"][0]["middleName"]
    except:
        p.owner_middle_name = None
    try:
        p.owner_last_name = pa["owners"][0]["lastName"]
    except:
        p.owner_last_name = None
    try:
        p.owner_type = pa["ownerType"]
    except:
        p.owner_type = None
    try:
        p.pbKey = pa["pbKey"]
    except:
        p.pkKey = None
    return p


def write_to_file(path, to_print):
    from inlyst_backend.settings import (
        BASE_DIR,
    )

    log_path = f"{BASE_DIR}/inlyst_backend/{path}"
    fd = open(log_path, "a")
    fd.write(to_print)
    fd.flush()
    fd.close()


def resetWizardAll():
    from listing.models import PersonalizedWizardStep

    PersonalizedWizardStep.objects.all().update(
        is_completed=None, last_step_completed=0
    )


def get_keyword_object():
    return [
        {"mystatemls_name": "ap_dishwasher", "name": "Appliance Dishwasher"},
        {"mystatemls_name": "ap_disposal", "name": "Appliance Garbage"},
        {"mystatemls_name": "ap_dryer", "name": "Appliance Dryer"},
        {"mystatemls_name": "ap_fridge", "name": "Appliance Refrigerator"},
        {"mystatemls_name": "ap_hot_water_heater", "name": "Appliance Hot Water"},
        {"mystatemls_name": "ap_microwave", "name": "Appliance Microwave"},
        {"mystatemls_name": "ap_oven", "name": "Appliance Oven"},
        {"mystatemls_name": "ap_stainless_steel", "name": "Appliance Stainless Steel"},
        {"mystatemls_name": "ap_washer", "name": "Appliance Washer"},
        {"mystatemls_name": "attic_access", "name": "Has Attic Access"},
        {"mystatemls_name": "basement_type", "name": "Basement Type"},
        {"mystatemls_name": "beds", "name": "Number of Bedrooms"},
        {"mystatemls_name": "biz_name", "name": "Business Name"},
        {"mystatemls_name": "bld_55over", "name": "Building/Community 55"},
        {"mystatemls_name": "bld_basement", "name": "Building Basement"},
        {"mystatemls_name": "bld_bike", "name": "Building/Community Bikes"},
        {"mystatemls_name": "bld_clubhouse", "name": "Building/Community"},
        {"mystatemls_name": "bld_concierge", "name": "Building/Community Concierge"},
        {"mystatemls_name": "bld_doorman", "name": "Building Doorman"},
        {"mystatemls_name": "bld_elevator", "name": "Building Elevator"},
        {"mystatemls_name": "bld_gated", "name": "Building/Community Gated"},
        {"mystatemls_name": "bld_golf", "name": "Building/Community Golf"},
        {"mystatemls_name": "bld_gym", "name": "Building/Community Gym"},
        {"mystatemls_name": "bld_laundry", "name": "Building/Community Laundry"},
        {"mystatemls_name": "bld_parking", "name": "Building/Community Parking"},
        {"mystatemls_name": "bld_pets", "name": "Building/Community Pets"},
        {"mystatemls_name": "bld_playground", "name": "Building/Community Playground"},
        {"mystatemls_name": "bld_pool", "name": "Building/Community Pool"},
        {"mystatemls_name": "bld_post_war", "name": "Post-War Building"},
        {"mystatemls_name": "bld_pre_war", "name": "Pre-War Building"},
        {"mystatemls_name": "bld_rec_room", "name": "Building/Community Rec Room"},
        {"mystatemls_name": "bld_rooftop", "name": "Building Rooftop"},
        {"mystatemls_name": "bld_sauna", "name": "Building/Community Sauna"},
        {"mystatemls_name": "bld_screening", "name": "Building/Community Screening"},
        {"mystatemls_name": "bld_security", "name": "Building/Community Security"},
        {"mystatemls_name": "bld_storage", "name": "Building/Community Storage"},
        {
            "mystatemls_name": "bld_tennis_court",
            "name": "Building/Community Tennis Court",
        },
        {"mystatemls_name": "bm_area", "name": "Basement Area Square"},
        {"mystatemls_name": "bm_baths", "name": "Basement Bathrooms"},
        {"mystatemls_name": "bm_beds", "name": "Basement Bedrooms"},
        {"mystatemls_name": "bm_bilco", "name": "Basement Bilco Doors"},
        {"mystatemls_name": "bm_finished", "name": "Basement Finished"},
        {"mystatemls_name": "bm_garage", "name": "Basement Garage"},
        {"mystatemls_name": "bm_kitchen", "name": "Basement Kitchen"},
        {"mystatemls_name": "bm_no_access", "name": "Basement No Access"},
        {"mystatemls_name": "bm_partly_finished", "name": "Basement Partly Finished"},
        {"mystatemls_name": "bm_unfinished", "name": "Basement Unfinished"},
        {"mystatemls_name": "bm_walkout", "name": "Basement Walkout"},
        {"mystatemls_name": "building_style", "name": "Building Style"},
        {"mystatemls_name": "central_ac", "name": "Has Central AC"},
        {"mystatemls_name": "ex_attached_park", "name": "Attached Parking"},
        {"mystatemls_name": "ex_corner", "name": "Corner Lot"},
        {"mystatemls_name": "ex_covered_porch", "name": "Exterior Covered Porch"},
        {"mystatemls_name": "ex_cul_de_sac", "name": "Cul de Sac"},
        {"mystatemls_name": "ex_deck", "name": "Exterior Deck"},
        {"mystatemls_name": "ex_driveway", "name": "Driveway"},
        {"mystatemls_name": "ex_enclosed_porch", "name": "Exterior Enclosed Porch"},
        {"mystatemls_name": "ex_equestrian", "name": "Equestrian Property"},
        {"mystatemls_name": "ex_exterior_material", "name": "Exterior Material"},
        {"mystatemls_name": "ex_fence", "name": "Exterior Fence"},
        {"mystatemls_name": "ex_golf", "name": "Exterior Golf"},
        {"mystatemls_name": "ex_open_porch", "name": "Exterior Open Porch"},
        {"mystatemls_name": "ex_outdoor_shower", "name": "Exterior Outdoor Shower"},
        {"mystatemls_name": "ex_patio", "name": "Exterior Patio"},
        {"mystatemls_name": "ex_permit", "name": "Permits"},
        {"mystatemls_name": "ex_room_for_garage", "name": "Room for Garage"},
        {"mystatemls_name": "ex_room_for_pool", "name": "Room for Pool"},
        {"mystatemls_name": "ex_room_for_tennis", "name": "Room for Tennis"},
        {"mystatemls_name": "ex_screen_porch", "name": "Exterior Screened Porch"},
        {"mystatemls_name": "ex_sprinkler_system", "name": "Exterior Sprinkler System"},
        {"mystatemls_name": "ex_subdivision", "name": "Subdivision Name"},
        {"mystatemls_name": "ex_survey", "name": "Survey"},
        {"mystatemls_name": "ex_tennis", "name": "Exterior Tennis"},
        {"mystatemls_name": "ex_tennis_court_surface", "name": "Tennis Court Surface"},
        {"mystatemls_name": "ex_trees", "name": "Trees"},
        {"mystatemls_name": "fireplaces", "name": "Number of Fireplaces"},
        {"mystatemls_name": "fl_carpet", "name": "Floor Carpet"},
        {"mystatemls_name": "fl_granite", "name": "Floor Granite"},
        {"mystatemls_name": "fl_hardwood", "name": "Floor Hardwood"},
        {"mystatemls_name": "fl_laminate", "name": "Floor Laminate"},
        {"mystatemls_name": "fl_linoleum", "name": "Floor Linoleum"},
        {"mystatemls_name": "fl_marble", "name": "Floor Marble"},
        {"mystatemls_name": "fl_stone", "name": "Floor Stone"},
        {"mystatemls_name": "fl_tile", "name": "Floor Tile"},
        {"mystatemls_name": "fl_vinyl", "name": "Floor Vinyl"},
        {"mystatemls_name": "floor_num", "name": "Floor Number of Unit"},
        {"mystatemls_name": "freight_elevators", "name": "Number Freight"},
        {"mystatemls_name": "full_baths", "name": "Number of Full Baths"},
        {"mystatemls_name": "furnished", "name": "Is Furnished?"},
        {"mystatemls_name": "garage_spaces", "name": "Number of Garage"},
        {"mystatemls_name": "garage_type", "name": "Garage Type"},
        {"mystatemls_name": "h2o_access", "name": "Waterfront Access"},
        {"mystatemls_name": "h2o_bay", "name": "Waterfront Bay"},
        {"mystatemls_name": "h2o_beach_rights", "name": "Waterfront Beach Rights"},
        {"mystatemls_name": "h2o_canal", "name": "Waterfront Canal"},
        {"mystatemls_name": "h2o_creek", "name": "Waterfront Creek"},
        {"mystatemls_name": "h2o_deep_water_dock", "name": "Waterfront Deep Water"},
        {"mystatemls_name": "h2o_dock", "name": "Waterfront Dock"},
        {"mystatemls_name": "h2o_dock_depth", "name": "Dock Depth"},
        {"mystatemls_name": "h2o_dock_rights", "name": "Waterfront Dock Rights"},
        {"mystatemls_name": "h2o_frontage", "name": "Water frontage"},
        {"mystatemls_name": "h2o_harbor", "name": "Waterfront Harbor"},
        {"mystatemls_name": "h2o_inlet", "name": "Waterfront Inlet"},
        {"mystatemls_name": "h2o_kill", "name": "Waterfront Kill"},
        {"mystatemls_name": "h2o_lake", "name": "Waterfront Lake"},
        {"mystatemls_name": "h2o_ocean", "name": "Waterfront Ocean"},
        {"mystatemls_name": "h2o_pond", "name": "Waterfront Pond"},
        {"mystatemls_name": "h2o_river", "name": "Waterfront River"},
        {"mystatemls_name": "h2o_sound", "name": "Waterfront Sound"},
        {"mystatemls_name": "h2o_stream", "name": "Waterfront Stream"},
        {"mystatemls_name": "h2o_water_name", "name": "Body of Water Name"},
        {"mystatemls_name": "half_baths", "name": "Number of Half Baths"},
        {"mystatemls_name": "hamlet_id", "name": "Hamlet ID"},
        {"mystatemls_name": "handicap", "name": "Handicap Features"},
        {"mystatemls_name": "has_loading_docks", "name": "Has Loading Docks"},
        {"mystatemls_name": "has_pool", "name": "Has Pool"},
        {"mystatemls_name": "hf_coal", "name": "Heat Fuel Coal"},
        {"mystatemls_name": "hf_electric", "name": "Heat Fuel Electric"},
        {"mystatemls_name": "hf_gas", "name": "Heat Fuel Gas"},
        {"mystatemls_name": "hf_kerosene", "name": "Heat Fuel Kerosene"},
        {"mystatemls_name": "hf_natural_gas", "name": "Heat Fuel Natural Gas"},
        {"mystatemls_name": "hf_oil", "name": "Heat Fuel Oil"},
        {"mystatemls_name": "hf_propane", "name": "Heat Fuel Propane"},
        {"mystatemls_name": "hf_solar", "name": "Heat Fuel Solar"},
        {"mystatemls_name": "hf_wood", "name": "Heat Fuel Wood"},
        {"mystatemls_name": "hidden", "name": "Is Listing Hidden"},
        {"mystatemls_name": "hoa", "name": "Is this a home owners"},
        {"mystatemls_name": "hoa_development", "name": "HOA Development Name"},
        {"mystatemls_name": "hoa_fee", "name": "HOA Fee"},
        {"mystatemls_name": "hoa_name", "name": "HOA Name"},
        {"mystatemls_name": "hoa_phone", "name": "HOA Phone"},
        {"mystatemls_name": "how_sold", "name": "How Sold"},
        {"mystatemls_name": "ht_baseboard", "name": "Heat Type Baseboard"},
        {"mystatemls_name": "ht_forced_air", "name": "Heat Type Forced Air"},
        {"mystatemls_name": "ht_geo_thermal", "name": "Heat Type Geo Thermal"},
        {"mystatemls_name": "ht_heat_ac_zones", "name": "Heat AC Zones"},
        {"mystatemls_name": "ht_hot_water", "name": "Heat Type Hot Water"},
        {"mystatemls_name": "ht_hydro_air", "name": "Heat Type Hydro Air"},
        {"mystatemls_name": "ht_no_heat", "name": "No Heat"},
        {"mystatemls_name": "ht_other", "name": "Heat Type Other"},
        {"mystatemls_name": "ht_pump", "name": "Heat Type Pump"},
        {"mystatemls_name": "ht_radiant", "name": "Heat Type Radiant"},
        {"mystatemls_name": "ht_steam", "name": "Heat Type Steam"},
        {"mystatemls_name": "in_alarm", "name": "Interior Alarm"},
        {"mystatemls_name": "in_amps", "name": "Interior Amps"},
        {"mystatemls_name": "in_sprinklers", "name": "Interior Sprinklers"},
        {"mystatemls_name": "in_staff_baths", "name": "Staff Bathrooms"},
        {"mystatemls_name": "in_staff_beds", "name": "Staff Bedrooms"},
        {"mystatemls_name": "inc_gross", "name": "Income Amount Gross"},
        {"mystatemls_name": "inc_net", "name": "Income Amount Net"},
        {"mystatemls_name": "is_absolute_auction", "name": "Is Absolute Auction"},
        {"mystatemls_name": "is_company_private", "name": "Is Company Private"},
        {"mystatemls_name": "is_extended", "name": "Is Extended Listing"},
        {"mystatemls_name": "is_land_lease", "name": "Is Land Lease"},
        {"mystatemls_name": "is_online_only_auction", "name": "Is Online Only Auction"},
        {"mystatemls_name": "is_live_only_auction", "name": "Is Live Only Auction"},
        {"mystatemls_name": "is_seasonal", "name": "Is Seasonal Rental"},
        {"mystatemls_name": "is_water_view", "name": "Is Water View"},
        {"mystatemls_name": "is_waterfront", "name": "Waterfront Property"},
        {"mystatemls_name": "mot_display_land", "name": "Display with Land Results"},
        {"mystatemls_name": "mot_estate", "name": "Sale Type Estate"},
        {"mystatemls_name": "mot_fixup", "name": "Sale Type Handy Man"},
        {"mystatemls_name": "mot_foreclosure", "name": "Sale Type Foreclosure"},
        {"mystatemls_name": "mot_holdpaper", "name": "Sale Type Will Hold"},
        {"mystatemls_name": "mot_preforeclosure", "name": "Sale Type Preforeclosure"},
        {"mystatemls_name": "mot_relocating", "name": "Sale Type Relocating"},
        {"mystatemls_name": "mot_shortsale", "name": "Sale Type Short Sale"},
        {"mystatemls_name": "mot_typical", "name": "Sale Type Typical"},
        {"mystatemls_name": "natural_gas", "name": "Is Natural Gas Available"},
        {"mystatemls_name": "near_bus", "name": "Near Bus"},
        {"mystatemls_name": "near_school", "name": "Near School"},
        {"mystatemls_name": "near_train", "name": "Near Train"},
        {"mystatemls_name": "neighborhood", "name": "Neighborhood Name"},
        {"mystatemls_name": "new_construction", "name": "New Construction"},
        {"mystatemls_name": "no_fee", "name": "No Fee Split typically"},
        {"mystatemls_name": "occupancy", "name": "Is Occupied"},
        {"mystatemls_name": "oh_barn", "name": "Outbuilding Barn"},
        {"mystatemls_name": "oh_cabana", "name": "Outbuilding Cabana"},
        {"mystatemls_name": "oh_carport", "name": "Outbuilding Carport"},
        {"mystatemls_name": "oh_general", "name": "Outbuilding General"},
        {"mystatemls_name": "oh_guest_house", "name": "Outbuilding Guest House"},
        {"mystatemls_name": "oh_gym", "name": "Outbuilding Gym"},
        {"mystatemls_name": "oh_office", "name": "Outbuilding Office"},
        {"mystatemls_name": "oh_pool_house", "name": "Outbuilding Pool House"},
        {"mystatemls_name": "oh_riding_ring", "name": "Outbuilding Riding Ring"},
        {"mystatemls_name": "oh_shed", "name": "Outbuilding Shed"},
        {"mystatemls_name": "oh_stable", "name": "Outbuilding Stable"},
        {"mystatemls_name": "oh_studio", "name": "Outbuilding Studio"},
        {"mystatemls_name": "oh_workshop", "name": "Outbuilding Workshop"},
        {"mystatemls_name": "owner_finance", "name": "Owner Financing"},
        {"mystatemls_name": "pool_above_ground", "name": "Pool Above Ground"},
        {"mystatemls_name": "pool_child_proof", "name": "Pool Child Proof"},
        {"mystatemls_name": "pool_gunite", "name": "Pool Gunite"},
        {"mystatemls_name": "pool_heated", "name": "Pool Heated"},
        {"mystatemls_name": "pool_in_ground", "name": "Pool Inground"},
        {"mystatemls_name": "pool_indoor", "name": "Pool Indoor"},
        {"mystatemls_name": "pool_infinity", "name": "Pool Infinity"},
        {"mystatemls_name": "pool_salt_water", "name": "Pool Salt Water"},
        {"mystatemls_name": "pool_sauna", "name": "Pool Sauna"},
        {"mystatemls_name": "pool_solar", "name": "Pool Solar"},
        {"mystatemls_name": "pool_spa", "name": "Pool Spa"},
        {"mystatemls_name": "pool_vinyl", "name": "Pool Vinyl"},
        {"mystatemls_name": "rent_internet", "name": "Internet"},
        {"mystatemls_name": "rent_landlord_show", "name": "Landlord Showing"},
        {"mystatemls_name": "rent_linens", "name": "Linens"},
        {"mystatemls_name": "rent_pets", "name": "Pets"},
        {"mystatemls_name": "rent_reg_expire_date", "name": "Registration Expiration"},
        {"mystatemls_name": "rent_reg_num", "name": "Rental Registration"},
        {"mystatemls_name": "rent_smoking", "name": "Smoking"},
        {"mystatemls_name": "rent_tv", "name": "TV"},
        {"mystatemls_name": "rentdate", "name": "Rent Date *REQUIRED IF RENTED*"},
        {"mystatemls_name": "rf_asphalt", "name": "Roof Asphalt"},
        {"mystatemls_name": "rf_cedar", "name": "Roof Cedar"},
        {"mystatemls_name": "rf_flat", "name": "Roof Flat"},
        {"mystatemls_name": "rf_metal", "name": "Roof Metal"},
        {"mystatemls_name": "rf_rubber", "name": "Roof Rubber"},
        {"mystatemls_name": "rf_slate", "name": "Roof Slate"},
        {"mystatemls_name": "rf_tar", "name": "Roof Tar"},
        {"mystatemls_name": "rf_tile", "name": "Roof Tile"},
        {"mystatemls_name": "rm_art_studio", "name": "Room Art Studio"},
        {"mystatemls_name": "rm_bonus", "name": "Room Bonus"},
        {"mystatemls_name": "rm_breakfast", "name": "Room Breakfast"},
        {"mystatemls_name": "rm_den", "name": "Room Den"},
        {"mystatemls_name": "rm_dining", "name": "Room Dining"},
        {"mystatemls_name": "rm_en_suite", "name": "Room en Suite"},
        {"mystatemls_name": "rm_family", "name": "Room Family"},
        {"mystatemls_name": "rm_first_floor_bath", "name": "Room First Floor Bath"},
        {"mystatemls_name": "rm_first_floor_master", "name": "Room First Floor Master"},
        {"mystatemls_name": "rm_formal", "name": "Room Formal"},
        {"mystatemls_name": "rm_foyer", "name": "Room Foyer"},
        {"mystatemls_name": "rm_great", "name": "Room Great"},
        {"mystatemls_name": "rm_gym", "name": "Room Gym"},
        {"mystatemls_name": "rm_kitchen", "name": "Room Kitchen"},
        {"mystatemls_name": "rm_laundry", "name": "Room Laundry"},
        {"mystatemls_name": "rm_library", "name": "Room Library"},
        {"mystatemls_name": "rm_living", "name": "Room Living"},
        {"mystatemls_name": "rm_loft", "name": "Room Loft"},
        {"mystatemls_name": "rm_master_bedroom", "name": "Room Master Bedroom"},
        {"mystatemls_name": "rm_media", "name": "Room Media"},
        {"mystatemls_name": "rm_private_guest", "name": "Room Private Guest"},
        {"mystatemls_name": "rm_study", "name": "Room Study"},
        {"mystatemls_name": "rm_walk_in_closet", "name": "Room Walkin Closet"},
        {"mystatemls_name": "saledate", "name": "Sale Date"},
        {"mystatemls_name": "sd_aluminum", "name": "Siding Aluminum"},
        {"mystatemls_name": "sd_asbestos", "name": "Siding Asbestos"},
        {"mystatemls_name": "sd_brick", "name": "Siding Brick"},
        {"mystatemls_name": "sd_cedar_clapboard", "name": "Siding Cedar Clapboard"},
        {"mystatemls_name": "sd_cedar_shake", "name": "Siding Cedar Shake"},
        {"mystatemls_name": "sd_cement", "name": "Siding Cement"},
        {"mystatemls_name": "sd_hardi", "name": "Siding Hardi"},
        {"mystatemls_name": "sd_log", "name": "Siding Log"},
        {"mystatemls_name": "sd_masonry", "name": "Siding Masonry"},
        {"mystatemls_name": "sd_stone", "name": "Siding Stone"},
        {"mystatemls_name": "sd_stucco", "name": "Siding Stucco"},
        {"mystatemls_name": "sd_t111", "name": "Siding T1-11"},
        {"mystatemls_name": "sd_vinyl", "name": "Siding Vinyl"},
        {"mystatemls_name": "sd_wood", "name": "Siding Wood"},
        {"mystatemls_name": "soh", "name": "South of the Highway"},
        {"mystatemls_name": "sprinklers", "name": "Has Sprinklers"},
        {"mystatemls_name": "st_pellet", "name": "Stove Pellet"},
        {"mystatemls_name": "st_propane", "name": "Stove Propane"},
        {"mystatemls_name": "st_wood", "name": "Stove Wood"},
        {"mystatemls_name": "uf_balcony", "name": "Balcony"},
        {"mystatemls_name": "uf_central_vac", "name": "Central Vac"},
        {"mystatemls_name": "uf_corner", "name": "Corner"},
        {"mystatemls_name": "uf_fire_escape", "name": "Fire Escape"},
        {"mystatemls_name": "uf_garden", "name": "Garden"},
        {"mystatemls_name": "uf_ground_floor", "name": "Ground Floor"},
        {"mystatemls_name": "uf_intercom", "name": "Intercom"},
        {"mystatemls_name": "uf_laundry", "name": "Laundry"},
        {"mystatemls_name": "uf_terrace", "name": "Terrace"},
        {"mystatemls_name": "uf_upper_floor", "name": "Upper Floor"},
        {"mystatemls_name": "undisclosed_address", "name": "Undisclosed Address"},
        {"mystatemls_name": "unit_num", "name": "Unit Number"},
        {"mystatemls_name": "A UNIT", "name": "LOT"},
        {"mystatemls_name": "up_cleaning", "name": "Is Cleaning Paid"},
        {"mystatemls_name": "up_electric", "name": "Is Electric Utilities Paid"},
        {"mystatemls_name": "up_gas", "name": "Is Gas Utilities Paid"},
        {"mystatemls_name": "up_ground_maint", "name": "Is Ground Maintenance"},
        {"mystatemls_name": "up_heat", "name": "Is Heat Utilities Paid"},
        {"mystatemls_name": "up_hvac", "name": "Is HVAC Paid"},
        {"mystatemls_name": "up_insurance", "name": "Is Insurance Paid"},
        {"mystatemls_name": "up_ord_maint", "name": "Is Ordinary Maintenance"},
        {"mystatemls_name": "up_parking", "name": "Is Parking Paid"},
        {"mystatemls_name": "up_struct_maint", "name": "Is Structural"},
        {"mystatemls_name": "up_water", "name": "Is Water Paid"},
        {"mystatemls_name": "vw_bay", "name": "View Bay"},
        {"mystatemls_name": "vw_canal", "name": "View Canal"},
        {"mystatemls_name": "vw_city", "name": "View City"},
        {"mystatemls_name": "vw_creek", "name": "View Creek"},
        {"mystatemls_name": "vw_harbor", "name": "View Harbor"},
        {"mystatemls_name": "vw_inlet", "name": "View Inlet"},
        {"mystatemls_name": "vw_lake", "name": "View Lake"},
        {"mystatemls_name": "vw_mountain", "name": "View Mountain"},
        {"mystatemls_name": "vw_ocean", "name": "View Ocean"},
        {"mystatemls_name": "vw_park", "name": "View Park"},
        {"mystatemls_name": "vw_pond", "name": "View Pond"},
        {"mystatemls_name": "vw_private", "name": "View Private"},
        {"mystatemls_name": "vw_river", "name": "View River"},
        {"mystatemls_name": "vw_scenic", "name": "View Scenic"},
        {"mystatemls_name": "vw_sound", "name": "View Sound"},
        {"mystatemls_name": "vw_stream", "name": "View Stream"},
        {"mystatemls_name": "vw_street", "name": "View Street"},
        {"mystatemls_name": "vw_water", "name": "View Water"},
        {"mystatemls_name": "vw_wooded", "name": "View Wooded"},
        {"mystatemls_name": "wallwin_ac", "name": "Wall/Window AC"},
        {"mystatemls_name": "is_community", "name": "Is a Community"},
        {"mystatemls_name": "is_hoa", "name": "Is HOA"},
        {"mystatemls_name": "bld_pre_war", "name": "Pre-War Building"},
        {"mystatemls_name": "bld_post_war", "name": "Post-War Building"},
        {"mystatemls_name": "bld_55over", "name": "Building/Community 55 And Over"},
        {"mystatemls_name": "hoa_fee", "name": "HOA Fee"},
        {"mystatemls_name": "cm_available_lots", "name": "Available Lots"},
        {"mystatemls_name": "cm_management_name", "name": "Property Management"},
        {"mystatemls_name": "is_condo", "name": "Is a Condo"},
        {"mystatemls_name": "is_coop", "name": "Is a Co-op"},
        {"mystatemls_name": "road_type", "name": "Amenities Road Type"},
        {"mystatemls_name": "driveway_type", "name": "Amenities Driveway Type"},
        {"mystatemls_name": "parking_spaces", "name": "Parking Spaces Included"},
        {"mystatemls_name": "add_parking_price", "name": "Additional Parking Space"},
        {"mystatemls_name": "has_guest_parking", "name": "Guest Parking"},
        {"mystatemls_name": "age_restriction", "name": "Age Restriction"},
        {"mystatemls_name": "is_dogs_allowed", "name": "Dogs allowed"},
        {"mystatemls_name": "is_cats_allowed", "name": "Cats allowed"},
        {"mystatemls_name": "is_other_allowed", "name": "Other pets allowed"},
        {"mystatemls_name": "pet_breed_restriction", "name": "Breed Restriction"},
        {"mystatemls_name": "pet_weight_restriction", "name": "Weight Restriction"},
        {"mystatemls_name": "pet_deposit", "name": "Pet Deposit?"},
        {"mystatemls_name": "pet_monthly_fee", "name": "Monthly Fee?"},
        {"mystatemls_name": "subletting_allowed", "name": "Subletting Allowed"},
        {"mystatemls_name": "owner_occupancy_required", "name": "Owner Occupancy"},
        {"mystatemls_name": "sublot_allowed", "name": "Sublot Allowed"},
    ]

def reset_order_cover_photo(listing):
    from listing.models import File
    files=File.objects.filter(listing=listing)
    
