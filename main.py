from app.chain import create_chain

def main():
    chain = create_chain()
    print("=== AI Resume Analyzer ===\n")

    print("Paste your Job Description (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    job_description = "\n".join(lines)

    print("\nPaste your Resume (press Enter twice when done):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    resume = "\n".join(lines)

    print("\nAnalyzing... please wait\n")
    result = chain.invoke({
        "job_description": job_description,
        "resume": resume
    })

    print(f"Match Score:        {result['match_score']}%")
    print(f"Matched Keywords:   {', '.join(result['matched_keywords'])}")
    print(f"Missing Keywords:   {', '.join(result['missing_keywords'])}")
    print(f"\nSuggestions:")
    for i, s in enumerate(result['suggestions'], 1):
        print(f"  {i}. {s}")
    print(f"\nOverall Feedback:   {result['overall_feedback']}")

if __name__ == "__main__":
    main()