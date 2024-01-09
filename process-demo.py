from prefect import flow


@flow(log_prints=True)
def print_hi():
    print("hey there!")


if __name__ == "__main__":
    print_issue.from_source(
        source="https://github.com/discdiver/process-demo.git",
        entrypoint="flow.py:print_issue",
    ).deploy(name="gh-process-deploy", work_pool_name="process1")
