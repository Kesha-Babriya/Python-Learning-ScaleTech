import asyncio
import time


# ============================================================
# Common async functions
# ============================================================

async def fetch_profile():

    print("Fetching profile...")

    await asyncio.sleep(2)

    print("Profile fetched successfully")

    return "Kesha"


async def fetch_marks():

    print("Fetching marks...")

    await asyncio.sleep(4)          #change second to see difference 

    print("Marks fetched successfully")

    return 98


# ============================================================
# PART 1: Using await one by one
# ============================================================

async def normal_await():

    print("\n--- PART 1: await one by one ---")

    start_time = time.time()

    # First function completely finishes
    profile = await fetch_profile()

    # Only after profile finishes, marks starts
    marks = await fetch_marks()

    end_time = time.time()

    print("Name:", profile)
    print("Marks:", marks)

    print(f"Total time: {end_time - start_time:.2f} seconds")


# ============================================================
# PART 2: Using asyncio.gather()
# ============================================================

async def using_gather():

    print("\n--- PART 2: asyncio.gather() ---")

    start_time = time.time()

    # Both functions can run concurrently
    profile, marks = await asyncio.gather(
        fetch_profile(),
        fetch_marks()
    )

    end_time = time.time()

    print("Name:", profile)
    print("Marks:", marks)

    print(f"Total time: {end_time - start_time:.2f} seconds")


# ============================================================
# Main program
# ============================================================

async def main():

    await normal_await()

    await using_gather()


# Start AsyncIO
asyncio.run(main())