import os
from dotenv import load_dotenv

load_dotenv()

cohort = os.getenv('cohort')

print(cohort)