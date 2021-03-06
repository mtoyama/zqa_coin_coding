from coinapi_rest_v1 import restapi

class OHLCVHistoricalDataRequestByAsset:
    def __init__(self, asset_id_base, asset_id_quote, query_parameters = dict()):
        self.asset_id_base = asset_id_base
        self.asset_id_quote = asset_id_quote
        self.query_parameters = query_parameters

    def endpoint(self):
        return f'/ohlcv/{self.asset_id_base}/{self.asset_id_quote}/history'

def ohlcv_historical_data_by_asset(self,
                                   asset_id_base,
                                   asset_id_quote,
                                   query_parameters):
    request = OHLCVHistoricalDataRequestByAsset(
        asset_id_base,
        asset_id_quote,
        query_parameters
    )
    client = self.client_class(request.endpoint(),
                                self.headers,
                                request.query_parameters)
    return client.perform()