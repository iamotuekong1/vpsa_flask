from flask_restful import Resource
from app.services import ebay, amazon, alibaba

class Search(Resource):
    def get(self, query):
        # Search logic for fetching products based on a query
        search_results = []
        search_results.extend(ebay.search_products(query))
        search_results.extend(amazon.search_products(query))
        search_results.extend(alibaba.search_products(query))

        # Optionally, optimize the results (e.g., rank by relevance, price)
        return {'results': search_results}, 200
