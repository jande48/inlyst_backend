

def populate_property_object(p, pa):
    try:
        p.property_type = pa["propType"]
    except:
        p.property_type = None
    try:
        p.building_type = pa["buildgType"]["value"]
    except:
        p.building_type =None
    try:
        p.square_footage = int(float(pa["buildgSqFt"]))
    except:
        p.square_footage = None
    try:
        p.living_square_footage = int(float(pa["livingSqFt"]))
    except:
        p.living_square_footage =None
    try:
        p.property_square_footage = int(float(pa["propSqFt"]))
    except:
        p.property_square_footage = None
    try:
        p.parking_square_footage = int(float(pa["parkingSqFt"]))
    except:
        p.parking_square_footage =None
    try:
        p.property_acres = pa["propAcres"]
    except:
        p.property_acres = None
    try:
        p.land_use = pa["landUse"]["value"]
    except:
        p.land_use =None
    try:
        p.roof_cover_type = pa["roofCoverType"]["value"]
    except:
        p.roof_cover_type = None
    try:
        p.subdivision_name = pa["subdivision"]
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
        p.tax_amount =None
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
        p.tax_address = pa["taxAddress"]
    except:
        p.tax_address = None
    try:
        p.main_address_line = pa["formattedTaxAddress"]["mainAddressLine"]
    except:
        p.main_address_line = None
    try:
        p.address_number = pa["formattedTaxAddress"]["addressNumber"]
    except:
        p.address_number = None
    try:
        p.street_name = pa["formattedTaxAddress"]["streetName"]
    except:
        p.street_name = None
    try:
        p.street_type = pa["formattedTaxAddress"]["streetType"]
    except:
        p.street_type = None
    try:
        p.city = pa["formattedTaxAddress"]["city"]
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
    return p