from prefect import flow, task, get_run_logger


@task(name="ToUpper", description="Test func to uppercase text")
def task_1(text):
    logger = get_run_logger()
    logger.warning("Converting to UPPER")
    return text.upper()


@task(name="NoWhitespace", description="Test func to eliminate spaces")
def task_2(text: str):
    logger = get_run_logger()
    logger.warning("Removing whitespace")
    return text.replace(" ", "")


@flow(name="Test Flow 1", description="Tutorial flow for testing")
def main_flow():
    logger = get_run_logger()
    logger.info("Running flow...")
    text = "Bob Ross God Emperor Of Dune"
    t1 = task_1(text)
    t2 = task_2(t1)
    logger.info("Finished")
    print(t2)


if __name__ == '__main__':
    main_flow()
