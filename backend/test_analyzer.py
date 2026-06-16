from app.agents.analyzer import Analyzer

analyzer = Analyzer()

results = analyzer.analyze_repository(
    "test_repo"
)

for error in results["errors"]:

    print(error)