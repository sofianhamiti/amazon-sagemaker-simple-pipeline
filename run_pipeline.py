import yaml
import argparse
import sagemaker
from model_build.pipeline import get_pipeline


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-execution", action="store_true")
    args, _ = parser.parse_known_args()

    # IAM ROLE
    iam_role = sagemaker.get_execution_role()

    # CONFIG
    with open("cfg.yaml") as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)

    # INSTANTIATE PIPELINE
    print("INSTANTIATE PIPELINE")
    pipeline = get_pipeline(iam_role=iam_role, cfg=config)
    print(pipeline.definition())
    
    # # CREATE/UPDATE PIPELINE IN SAGEMAKER
    # logging.info("CREATE/UPDATE PIPELINE IN SAGEMAKER")
    # pipeline.upsert(role_arn=iam_role)

    # if args.run_execution:
    #     # RUN PIPELINE
    #     logging.info("RUNNING PIPELINE")
    #     pipeline.start()
