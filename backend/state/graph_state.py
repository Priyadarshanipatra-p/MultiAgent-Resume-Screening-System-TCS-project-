from typing import Annotated, Dict, List, Optional, TypedDict

from pydantic import Field


class ResumeInput(TypedDict, total=False):
    file_path: Annotated[str, Field(description="Uploaded resume file path")]
    file_name: Annotated[str, Field(description="Uploaded resume file name")]
    raw_text: Annotated[str, Field(description="Text extracted by document parser agent")]


class JobInput(TypedDict, total=False):
    job_description: Annotated[str, Field(description="Job description text")]
    required_skills: Annotated[List[str], Field(description="Required skills from the JD")]
    preferred_skills: Annotated[List[str], Field(description="Preferred skills from the JD")]
    role_level: Annotated[str, Field(description="Candidate profile or target role level")]


class ScreeningAgentState(TypedDict, total=False):
    candidate_name: Annotated[Optional[str], Field(description="Candidate name extracted from resume")]
    email: Annotated[Optional[str], Field(description="Candidate email extracted from resume")]
    phone: Annotated[Optional[str], Field(description="Candidate phone extracted from resume")]
    summary: Annotated[str, Field(description="Short resume summary")]
    skills: Annotated[List[str], Field(description="Skills extracted from resume")]
    experience: Annotated[List[str], Field(description="Relevant work experience")]
    education: Annotated[List[str], Field(description="Education details")]
    projects: Annotated[List[str], Field(description="Project details")]


class JDMatchingScoringAgentState(TypedDict, total=False):
    fit_score: Annotated[float, Field(description="Overall fit score from 0 to 100")]
    ranking: Annotated[Optional[int], Field(description="Candidate ranking if multiple resumes are compared")]
    matched_skills: Annotated[List[str], Field(description="Skills matching the JD")]
    missing_skills: Annotated[List[str], Field(description="JD skills missing from resume")]
    recommendation: Annotated[str, Field(description="Shortlist recommendation")]
    reasoning: Annotated[str, Field(description="Reason for score and recommendation")]


class SkillGapAgentState(TypedDict, total=False):
    skill_gaps: Annotated[List[str], Field(description="Important missing skills")]
    learning_suggestions: Annotated[List[str], Field(description="Suggested learning or improvement areas")]
    gap_report: Annotated[str, Field(description="Readable skill gap report")]


class InterviewQuestion(TypedDict, total=False):
    question: Annotated[str, Field(description="Interview question")]
    category: Annotated[str, Field(description="Question category")]
    difficulty: Annotated[str, Field(description="Question difficulty")]


class InterviewQuestionAgentState(TypedDict, total=False):
    questions: Annotated[List[InterviewQuestion], Field(description="Generated interview question bank")]


class GuardrailBiasAgentState(TypedDict, total=False):
    is_safe: Annotated[bool, Field(description="Whether generated content is safe and unbiased")]
    bias_flags: Annotated[List[str], Field(description="Bias or fairness issues found")]
    final_questions: Annotated[List[InterviewQuestion], Field(description="Guardrail-approved interview questions")]


class FeedbackReportAgentState(TypedDict, total=False):
    feedback: Annotated[str, Field(description="Personalized candidate feedback")]
    report_path: Annotated[Optional[str], Field(description="Generated feedback PDF path")]


class GraphState(TypedDict, total=False):
    resume: Annotated[ResumeInput, Field(description="Resume upload and parsed text")]
    job: Annotated[JobInput, Field(description="Job description and role input")]

    screening: Annotated[ScreeningAgentState, Field(description="Resume screening agent output")]
    scoring: Annotated[JDMatchingScoringAgentState, Field(description="JD matching and scoring output")]
    skill_gap: Annotated[SkillGapAgentState, Field(description="Skill gap analysis output")]
    interview_questions: Annotated[InterviewQuestionAgentState, Field(description="Interview question generation output")]
    guardrails: Annotated[GuardrailBiasAgentState, Field(description="Guardrail and bias detection output")]
    feedback_report: Annotated[FeedbackReportAgentState, Field(description="Feedback and report output")]

    ragas_metrics: Annotated[Dict[str, float], Field(description="RAGAS evaluation metrics")]
    errors: Annotated[List[str], Field(description="Errors collected during graph execution")]


