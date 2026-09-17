# A coroutine is a function that can pause its execution and later continue from where it stopped.

import asyncio


# ============================================================
# 1. COROUTINE FUNCTION
# ============================================================

async def fetch_profile():
    print("Fetching profile...")

    # Coroutine pauses here while waiting
    await asyncio.sleep(2)

    print("Profile fetched")

    # Coroutine can return a normal value
    return "Kesha"


# ============================================================
# 2. ANOTHER COROUTINE FUNCTION
# ============================================================

async def fetch_marks():
    print("Fetching marks...")

    await asyncio.sleep(3)

    print("Marks fetched")

    return 98


# ============================================================
# 3. COROUTINE WITH EXCEPTION
# ============================================================

async def fetch_result():
    print("Fetching result...")

    await asyncio.sleep(1)

    # Deliberately creating an error
    raise ValueError("Result service failed")


# ============================================================
# 4. USING await
# ============================================================

async def await_example():

    print("\n===== USING await ONE BY ONE =====")

    # First coroutine runs and finishes
    profile = await fetch_profile()

    # Only after profile finishes, marks starts
    marks = await fetch_marks()

    print("Profile:", profile)
    print("Marks:", marks)


# ============================================================
# 5. USING asyncio.gather()
# ============================================================

async def gather_example():

    print("\n===== USING asyncio.gather() =====")

    # Both coroutines can run concurrently
    profile, marks = await asyncio.gather(
        fetch_profile(),
        fetch_marks()
    )

    # gather() gives us their return values
    print("Profile:", profile)
    print("Marks:", marks)


# ============================================================
# 6. EXCEPTION HANDLING WITH await
# ============================================================

async def exception_example():

    print("\n===== EXCEPTION HANDLING =====")

    try:
        result = await fetch_result()
        print("Result:", result)

    except ValueError as error:
        print("Error:", error)


# ============================================================
# 7. CREATE TASK
# ============================================================

async def task_example():

    print("\n===== USING create_task() =====")

    # Create tasks from coroutines
    profile_task = asyncio.create_task(fetch_profile())
    marks_task = asyncio.create_task(fetch_marks())

    print("Tasks created")

    # Wait for the tasks and get their return values
    profile = await profile_task
    marks = await marks_task

    print("Profile:", profile)
    print("Marks:", marks)


# ============================================================
# 8. MAIN COROUTINE
# ============================================================

async def main():

    await await_example()

    await gather_example()

    await exception_example()

    await task_example()


# ============================================================
# 9. START ASYNCIO
# ============================================================

asyncio.run(main())