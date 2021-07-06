from infra.api.rest_client import restClient


class ProjectsApi(restClient):

    def __init__(self,base_url):
        super().__init__(base_url)

    def get_project(self,path,project_id,expected_status_code):
        response = self.get(f'{path}{project_id}',expected_status_code)
        return response.json()

    def check_project_delete(self,path,project_id,expected_status_code):
        self.get(f'{path}{project_id}',expected_status_code)


    def get_work_package(self,path,expected_status_code):
        response=self.get(f'{path}',expected_status_code)
        return response.json()

    def update_project(self,path,project_id,payload,expected_status_code):
        response=self.patch(f'{path}{project_id}',payload,expected_status_code)
        return response.json()

    def post_project(self,path,payload,expected_status_code):
        response=self.post(f'{path}',payload,expected_status_code)
        return response.json()


    def create_work_project_in_project(self,path,payload,expected_status_code):
        response=self.post(f'{path}',payload,expected_status_code)
        return response.json()

    def delete_project(self,path,project_id,expected_status_code):
        self.delete(f'{path}{project_id}',expected_status_code)


