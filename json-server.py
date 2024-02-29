from http.server import HTTPServer
from nss_handler import HandleRequests, status
import json

from views import get_all_orders, get_single_order, create_order, delete_order
from views import update_metal

class JSONServer(HandleRequests):

    def do_GET(self):
        response_body = ""
        url = self.parse_url(self.path)

        if url["requested_resource"] == "orders":
            if url["pk"] != 0:
                response_body = get_single_order(url["pk"])
                return self.response(response_body, status.HTTP_200_SUCCESS.value)

            response_body = get_all_orders()
            return self.response(response_body, status.HTTP_200_SUCCESS.value)
        
    def do_POST(self):
        url = self.parse_url(self.path)

        content_len = int(self.headers.get('content-length', 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "orders":
            if url["pk"] == 0:
                successful_post = create_order(request_body)
                if successful_post: 
                    return self.response("", status.HTTP_201_SUCCESS_CREATED.value)

    def do_DELETE(self):
        url = self.parse_url(self.path)

        if url["requested_resource"] == "orders":
            if url["pk"] != 0:
                successful_delete = delete_order(url["pk"])
                if successful_delete:
                    return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
                return self.response("Requested resource not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
        else: 
            return("Not Found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
        
    def do_PUT(self):
        url = self.parse_url(self.path)

        content_len = int(self.headers.get('content-length', 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "metals":
            if url["pk"] != 0:
                successful_post = update_metal(url["pk"], request_body)
                if successful_post:
                    return self.response("", status.HTTP_204_SUCCESS_NO_RESPONSE_BODY.value)
                else:
                    return self.response("Requested resource not found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)
        else:
            return self.response("Not Found", status.HTTP_404_CLIENT_ERROR_RESOURCE_NOT_FOUND.value)



def main():
    host = ''
    port = 8088
    HTTPServer((host, port), JSONServer).serve_forever()

if __name__ == "__main__":
    main()