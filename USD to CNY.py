def usdcny(usd):
    conversion_rate = 6.75
    cny = usd * conversion_rate
    return '{:.2f} Chinese Yuan'.format(cny)