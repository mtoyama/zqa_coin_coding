from coinapi_rest_v1 import restapi

# Get API data by asset pair rather than symbol string.
# REST: 
# GET /v1/ohlcv/{asset_id_base}/{asset_id_quote}/history?period_id={period_id}&time_start={time_start}&time_end={time_end}&limit={limit}&include_empty_items={include_empty_items}
# Reference: https://docs.coinapi.io/#historical-data
class OHLCVHistoricalDataRequestByAsset:
    def __init__(self, asset_id_base, asset_id_quote, query_parameters = dict()):
        self.asset_id_base = asset_id_base
        self.asset_id_quote = asset_id_quote
        self.query_parameters = query_parameters

    def endpoint(self):
        return f'/ohlcv/{self.asset_id_base}/{self.asset_id_quote}/history'

class OHLCVLatestDataRequestByAsset:
    def __init__(self, asset_id_base, asset_id_quote, query_parameters = dict()):
        self.asset_id_base = asset_id_base
        self.asset_id_quote = asset_id_quote
        self.query_parameters = query_parameters

    def endpoint(self):
        return f'/ohlcv/{self.asset_id_base}/{self.asset_id_quote}/latest'

class CoinAPIv1Patched(restapi.CoinAPIv1):
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

    def ohlcv_latest_data_by_asset(self,
                                asset_id_base,
                                asset_id_quote,
                                query_parameters):
        request = OHLCVLatestDataRequestByAsset(
            asset_id_base,
            asset_id_quote,
            query_parameters
        )
        client = self.client_class(request.endpoint(),
                                    self.headers,
                                    request.query_parameters)
        return client.perform()