# Databricks notebook source
# MAGIC %md 
# MAGIC ## Demo bundle configuration
# MAGIC Please ignore / do not delete, only used to prep and bundle the demo

# COMMAND ----------

{
  "name": "lakehouse-iot-platform",
  "category": "lakehouse",
  "serverless_supported": True,
  "custom_schema_supported": True,
  "default_schema": "dbdemos_iot_platform",
  "default_catalog": "main",
  "title": "Data Intelligence Platform for IoT & Prescriptive Maintenance",
  "description": "Detect faulty wind turbine and generate work orders: Ingestion (DLT), BI, Predictive Maintenance (ML), Prescriptive Maintenance (GenAI), Governance (UC), Orchestration",
    "fullDescription": "The Databricks Data Intelligence Platform allows your entire organization to use data and AI. It’s built on a lakehouse to provide an open, unified foundation for all data and governance, and is powered by a Data Intelligence Engine that understands the uniqueness of your data. In this demo, we'll show you how to build an IOT platform for prescriptive maintenance, ingesting sensor data from our wind turbine farm in realtime. We'll be able to deliver data and insights that would typically take months of effort on legacy platforms. <br/><br/>This demo covers the end to end data intelligence platform: <ul><li>Ingest data from external systems in streaming (sensors/ERP and then transform it using Delta Live Tables (DLT), a declarative ETL framework for building reliable, maintainable, and testable data processing pipelines. </li><li>Secure your ingested data to ensure governance and security</li><li>Leverage Databricks SQL and the warehouse endpoints to build dashboards to analyze the ingested data and our wind farm productivity</li><li>Build a Machine Learning model with Databricks AutoML to detect faulty wind turbines and trigger predictive maintenance operations</li><li Build an AI agent with the Mosaic AI Agent Framework to generate prescriptive work orders for wind turbines detected to be faulty</li><li>Orchestrate all these steps with Databricks Workflow</li></ul>",
  "usecase": "Data Intelligence Platform",
  "products": ["Delta Live Tables", "Databricks SQL", "MLFLow", "Auto ML", "Unity Catalog", "Spark"],
  "related_links": [
      {"title": "View all Product demos", "url": "<TBD: LINK TO A FILTER WITH ALL DBDEMOS CONTENT>"}, 
      {"title": "Databricks for Manufacturing", "url": "https://www.databricks.com/solutions/industries/manufacturing-industry-solutions"}],
  "recommended_items": ["lakehouse-fsi-credit", "lakehouse-fsi-fraud", "lakehouse-retail-c360"],
  "demo_assets": [
      {"title": "Delta Live Tables pipeline", "url": "https://www.dbdemos.ai/assets/img/dbdemos/lakehouse-iot-platform-dlt-0.png"},
      {"title": "Databricks SQL Dashboard: Wind Turbine predictive Maintenance", "url": "https://www.dbdemos.ai/assets/img/dbdemos/lakehouse-iot-platform-dashboard-0.png"},
      {"title": "Databricks SQL Dashboard: Turbine Analysis", "url": "https://www.dbdemos.ai/assets/img/dbdemos/lakehouse-iot-platform-dashboard-1.png"}], 
  "bundle": True,
  "tags": [{"dlt": "Delta Live Table"},  {"ds": "Data Science"}, {"uc": "Unity Catalog"}, {"dbsql": "BI/DW/DBSQL"}],
  "notebooks": [
    {
      "path": "_resources/00-setup", 
      "pre_run": False, 
      "publish_on_website": False, 
      "add_cluster_setup_cell": False,
      "title":  "Dbsql data", 
      "description": "Prep data for dbsql dashboard."
    },
    {
      "path": "_resources/01-load-data", 
      "pre_run": False, 
      "publish_on_website": False, 
      "add_cluster_setup_cell": False,
      "title":  "Load raw data", 
      "description": "Load raw data in dbfs."
    },
    {
      "path": "config", 
      "pre_run": False, 
      "publish_on_website": False, 
      "add_cluster_setup_cell": False,
      "title":  "Configuration file", 
      "description": "Define the database and volume folder."
    },
    {
      "path": "00-IOT-wind-turbine-introduction-DI-platform", 
      "pre_run": False,
      "publish_on_website": True, 
      "add_cluster_setup_cell": False,
      "title":  "Data Intelligence Platform - IOT Platform introduction", 
      "description": "Start here to explore the Data Intelligence Platform."
    },
    {
      "path": "01-Data-ingestion/01.1-DLT-Wind-Turbine-SQL", 
      "pre_run": False, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": False,
      "title":  "Ingest data with Delta Live Table", 
      "description": "SQL DLT pipeline to ingest data & build clean tables."
    },
    {
      "path": "01-Data-ingestion/01.2-DLT-Wind-Turbine-SQL-UDF", 
      "pre_run": False, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": False,
      "title":  "Ingest data with DLT-companion UDF", 
      "description": "Loads ML model as UDF in python."
    },
    {
      "path": "01-Data-ingestion/plain-spark-delta-pipeline/01.5-Delta-pipeline-spark-iot-turbine", 
      "pre_run": True, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": False,
      "title":  "Alternative: Ingest data with Spark+Delta", 
      "description": "Build a complete ingestion pipeline using spark API (alternative to DLT)"
    },
    {
      "path": "02-Data-governance/02-UC-data-governance-security-iot-turbine", 
      "pre_run": True, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": True,
      "title":  "Governance with Unity Catalog", 
      "description": "Secure your tables, lineage, auditlog..."
    },
     {
      "path": "03-BI-data-warehousing/03-BI-Datawarehousing-iot-turbine", 
      "pre_run": False, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": False,
      "title":  "Datawarehousing & BI / Dashboarding", 
      "description": "Run interactive queries on top of your data"
    },
    {
      "path": "04-Data-Science-ML/04.1-automl-iot-turbine-predictive-maintenance", 
      "pre_run": True, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": True,
      "title":  "Build predictive maintenance model (AutoML)", 
      "description": "Leverage Databricks AutoML to create a predictive maintenance model in a few clicks"
    },
    {
      "path": "04-Data-Science-ML/04.2-automl-generated-notebook-iot-turbine",
      "pre_run": True, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": True,
      "title":  "Explore predictive maintenance generated model", 
      "description": "Explore the best predictive maintenance model generated by AutoML and deploy it in production.",
      "parameters": {"shap_enabled": "false"}
    },
    {
      "path": "04-Data-Science-ML/04.3-running-inference-iot-turbine", 
      "pre_run": True, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": True,
      "title":  "Infer default probability in batch or realtime serverless", 
      "description": "Once your model is deployed, run low latency inferences."
    },
    {
      "path": "05-Generative-AI/05.1-ai-tools-iot-turbine-prescriptive-maintenance", 
      "pre_run": False, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": False,
      "title":  "Build AI agent tools with UC functions", 
      "description": "Use tools to enable the AI agent to perform actions besides language generation."
    },
    {
      "path": "05-Generative-AI/05.2-agent-creation-guide", 
      "pre_run": True, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": False,
      "title":  "Deploy your agents.", 
      "description": "Use Databricks Playground to test and deploy your agent."
    },
    {
      "path": "06-Workflow-orchestration/06-Workflow-orchestration-iot-turbine", 
      "pre_run": False, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": False,
      "title":  "Orchestrate predictive maintenance with Workflow", 
      "description": "Orchestrate all tasks in a job and schedule your data/model refresh"
    }
  ],
  "init_job": {
    "settings": {
        "name": "dbdemos_data_intelligence_platform_iot_turbine_init_{{CURRENT_USER_NAME}}",
        "email_notifications": {
            "no_alert_for_skipped_runs": False
        },
        "timeout_seconds": 0,
        "max_concurrent_runs": 1,
        "tasks": [
            {
                "task_key": "init_data",
                "notebook_task": {
                    "notebook_path": "{{DEMO_FOLDER}}/_resources/01-load-data",
                    "source": "WORKSPACE"
                },
                "job_cluster_key": "Shared_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "start_dlt_pipeline",
                "pipeline_task": {
                    "pipeline_id": "{{DYNAMIC_DLT_ID_dlt-iot-wind-turbine}}",
                    "full_refresh": true
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "depends_on": [
                    {
                        "task_key": "init_data"
                    }
                ]
            },
            {
                "task_key": "create_feature_and_automl_run",
                "notebook_task": {
                    "notebook_path": "{{DEMO_FOLDER}}/04-Data-Science-ML/04.1-automl-iot-turbine-predictive-maintenance",
                    "source": "WORKSPACE"
                },
                "job_cluster_key": "Shared_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {},
                "depends_on": [
                      {
                          "task_key": "start_dlt_pipeline"
                      }
                  ]
            },
            {
                "task_key": "deploy_best_model",
                "notebook_task": {
                    "notebook_path": "{{DEMO_FOLDER}}/04-Data-Science-ML/04.2-automl-generated-notebook-iot-turbine",
                    "source": "WORKSPACE"
                },
                "job_cluster_key": "Shared_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {},
                "depends_on": [
                      {
                          "task_key": "create_feature_and_automl_run"
                      }
                  ]
            },
            {
                "task_key": "deploy_endpoint",
                "notebook_task": {
                    "notebook_path": "{{DEMO_FOLDER}}/04-Data-Science-ML/04.3-running-inference-iot-turbine",
                    "source": "WORKSPACE"
                },
                "job_cluster_key": "Shared_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {},
                "depends_on": [
                      {
                          "task_key": "deploy_best_model"
                      }
                  ]
            }
        ],
        "job_clusters": [
            {
                "job_cluster_key": "Shared_job_cluster",
                "new_cluster": {
                    "spark_version": "16.4.x-cpu-ml-scala2.12",
                    "spark_conf": {
                        "spark.master": "local[*, 4]",
                        "spark.databricks.cluster.profile": "singleNode"
                    },
                    "custom_tags": {
                        "ResourceClass": "SingleNode"
                    },
                    "spark_env_vars": {
                        "PYSPARK_PYTHON": "/databricks/python3/bin/python3"
                    },
                    "enable_elastic_disk": True,
                    "data_security_mode": "SINGLE_USER",
                    "runtime_engine": "STANDARD",
                    "num_workers": 0
                }
            }
        ],
        "format": "MULTI_TASK"
    }
  },
  "cluster": {
      "spark_version": "16.4.x-cpu-ml-scala2.12",
      "spark_conf": {
        "spark.master": "local[*]",
        "spark.databricks.cluster.profile": "singleNode"
    },
    "custom_tags": {
        "ResourceClass": "SingleNode"
    },
    "single_user_name": "{{CURRENT_USER}}",
    "data_security_mode": "SINGLE_USER",
    "num_workers": 0
  }, 
  "pipelines": [
    {
      "id": "dlt-iot-wind-turbine",
      "run_after_creation": False,
      "definition": {
        "clusters": [
            {
                "label": "default",
                "autoscale": {
                    "min_workers": 1,
                    "max_workers": 2,
                    "mode": "ENHANCED"
                }
            }
        ],
        "development": True,
        "continuous": False,
        "channel": "PREVIEW",
        "edition": "ADVANCED",
        "photon": False,
        "libraries": [
            {
                "notebook": {
                    "path": "{{DEMO_FOLDER}}/01-Data-ingestion/01.1-DLT-Wind-Turbine-SQL"
                }
            },
            {
                "notebook": {
                    "path": "{{DEMO_FOLDER}}/01-Data-ingestion/01.2-DLT-Wind-Turbine-SQL-UDF"
                }
            }
        ],
        "name": "dbdemos_dlt_iot_turbine_{{CATALOG}}_{{SCHEMA}}",
        "catalog": "{{CATALOG}}",
        "target": "{{SCHEMA}}"
      }
    }
  ],
  "dashboards": [{"name": "[dbdemos] IOT - Turbine analysis",                    "id": "turbine-analysis"},
                 {"name": "[dbdemos] IOT - Wind Turbine predictive maintenance", "id": "turbine-predictive"}]
}
