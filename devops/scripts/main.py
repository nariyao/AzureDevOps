# Power BI Actions

import json
import os


class PowerBIActions:
    def __init__(self,env):
        self.env = env
        self.config = self.get_config("../configs/powerbi_config.json")
        self.authenticate()

    def authenticate(self):
        # Logic to authenticate with Power BI service
        print(f"Authenticating for environment: {self.env}")
        # Simulate authentication success
        return True

    def get_config(self, config_path=None):
        try:
            if not config_path:
                base_dir = os.path.dirname(os.path.abspath(__file__))
                config_path = os.path.join(base_dir, config_path)

            print(f"Reading configuration from {config_path}")
            
            with open(config_path, "r") as file:
                try:
                    full_config = json.load(file)
                except json.JSONDecodeError as e:
                    raise ValueError(f"Invalid JSON format in config file: {e}")
                
                config = full_config.get(self.env, {})
                if not config:
                    raise ValueError(f"No configuration found for environment: {self.env}")
                
                print(f"Configuration loaded: {config}")
                return config
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at path: {config_path}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error while loading config: {e}")

    def publish_report(self):
        report_path = self.config.get("reports_path", "")
        workspace_id = self.config.get("workspace", "")
        if not report_path or not workspace_id:
            raise ValueError("Report path or workspace ID is missing in the configuration.")
        print(f"Report path: {report_path}, Workspace ID: {workspace_id}")

    def refresh_dataset(self, dataset_id):
        # Logic to refresh a Power BI dataset
        print(f"Refreshing dataset with ID {dataset_id}")

    def get_report_details(self, report_id):
        # Logic to get details of a Power BI report
        print(f"Getting details for report with ID {report_id}")
        return {"report_id": report_id, "name": "Sample Report", "created_by": "User"}
    
    def delete_report(self, report_id):
        # Logic to delete a Power BI report
        print(f"Deleting report with ID {report_id}")

    def take_ownership(self, report_id, new_owner):
        # Logic to take ownership of a Power BI report
        print(f"Taking ownership of report {report_id} by {new_owner}")

    def list_reports(self, workspace_id):
        # Logic to list all reports in a Power BI workspace
        print(f"Listing reports in workspace {workspace_id}")
        return [{"report_id": "1", "name": "Report 1"}, {"report_id": "2", "name": "Report 2"}]
    
    def update_parameters(self, report_id, parameters):
        # Logic to update parameters of a Power BI report
        print(f"Updating parameters for report {report_id} with {parameters}")

    def bind_to_gateway(self, dataset_id, gateway_id):
        # Logic to bind a dataset to a Power BI gateway
        print(f"Binding dataset {dataset_id} to gateway {gateway_id}")

    def bind_to_datasource(self, dataset_id, datasource_id):
        # Logic to bind a dataset to a Power BI datasource
        print(f"Binding dataset {dataset_id} to datasource {datasource_id}")