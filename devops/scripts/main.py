# Power BI Actions

import json
import os


class PowerBIActions:
    def print_log(self, message, status_code=0):
        if status_code == 0:
            print(f"INFO: {message}")
        elif status_code == 1:
            print(f"WARNING: {message}")
        elif status_code == 2:
            print(f"ERROR: {message}")
        elif status_code == 3:
            print(f"CRITICAL: {message}")
        elif status_code == 4:
            if os.getenv("DEBUG_MODE", "false").lower() == "true":
                print(f"DEBUG: {message}")

    def __init__(self, env):
        self.env = env
        self.config = self.get_config("../configs/powerbi_config.json")
        self.authenticate()

    def validate_config(self):
        required_keys = ["workspace", "report_id", "dataset_id", "gateway_id"]
        missing_keys = [key for key in required_keys if key not in self.config]
        if missing_keys:
            raise ValueError(f"Missing required config keys: {', '.join(missing_keys)}")
        self.print_log("Configuration validated successfully.")

    def authenticate(self):
        client_id = os.getenv("POWER_BI_CLIENT_ID")
        client_secret = os.getenv("POWER_BI_CLIENT_SECRET")

        if not client_id or not client_secret:
            raise ValueError("Missing Power BI client credentials.")
        self.print_log("Power BI client credentials found.", status_code=4)
        self.print_log("Authenticating with Power BI service...", status_code=4)
        print(f"Client ID: {client_id}")
        print(f"Client Secret: {'*' * len(client_secret)}")
        # Logic to authenticate with Power BI service
        self.print_log("Authenticating with Power BI service...")
        # Simulate authentication success
        return True

    def get_config(self, config_path=None):
        try:
            if config_path:
                self.print_log(f"Using provided config path: {config_path}")
                base_dir = os.path.dirname(os.path.abspath(__file__))
                config_path = os.path.join(base_dir, config_path)
            else:
                raise ValueError("Configuration path must be provided.")
            
            self.print_log(f"Reading configuration from {config_path}")

            with open(config_path, "r") as file:
                try:
                    self.print_log("Parsing JSON configuration...", status_code=4)
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

    def publish_report(self, report_type="reports"):
        report_path = self.config.get(report_type, "")
        self.print_log(f"Publishing report from path: {report_path}")
        if not report_path:
            raise ValueError(f"Report path for type '{report_type}' is missing in the configuration.")
        if not os.path.exists(report_path):
            raise FileNotFoundError(f"Report path does not exist: {report_path}")
        if not os.path.isdir(report_path):
            raise NotADirectoryError(f"Report path is not a directory: {report_path}")
        if not os.listdir(report_path):
            self.print_log(f"Warning: Report directory is empty: {report_path}", status_code=1)
            return
        workspace_id = self.config.get("workspace", "")
        if not report_path or not workspace_id:
            raise ValueError("Report path or workspace ID is missing in the configuration.")
        self.print_log(f"Report path: {report_path}, Workspace ID: {workspace_id}")

    def refresh_dataset(self, dataset_id):
        # Logic to refresh a Power BI dataset
        self.print_log(f"Refreshing dataset with ID {dataset_id}")

    def get_report_details(self, report_id):
        # Logic to get details of a Power BI report
        self.print_log(f"Getting details for report with ID {report_id}")
        return {"report_id": report_id, "name": "Sample Report", "created_by": "User"}
    
    def delete_report(self, report_id):
        # Logic to delete a Power BI report
        self.print_log(f"Deleting report with ID {report_id}")

    def take_ownership(self, report_id, new_owner):
        # Logic to take ownership of a Power BI report
        self.print_log(f"Taking ownership of report {report_id} by {new_owner}")

    def list_reports(self):
        workspace_id = self.config.get("workspace", "")
        if not workspace_id:
            raise ValueError("Workspace ID is missing in the configuration.")
        # Logic to list all reports in a Power BI workspace
        self.print_log(f"Listing reports in workspace {workspace_id}")
        return [{"report_id": "1", "name": "Report 1"}, {"report_id": "2", "name": "Report 2"}]
    
    def update_parameters(self):
        report_id = self.config.get("report_id", "test-report-id")
        parameters = self.config.get("parameters", {"param1": "value1"})
        # Logic to update parameters of a Power BI report
        self.print_log(f"Updating parameters for report {report_id} with {parameters}")

    def update_gateways(self):
        # Logic to update Power BI gateways
        self.print_log("Updating Power BI gateways...")
        # Add your gateway update logic here
        self.print_log("Power BI gateways updated successfully.")

    def bind_to_gateway(self):
        dataset_id = self.config.get("dataset_id", "test-dataset-id")
        gateway_id = self.config.get("gateway_id", "test-gateway-id")
        # Logic to bind a dataset to a Power BI gateway
        self.print_log(f"Binding dataset {dataset_id} to gateway {gateway_id}")
        # Add your binding logic here
        self.print_log(f"Dataset {dataset_id} successfully bound to gateway {gateway_id}")