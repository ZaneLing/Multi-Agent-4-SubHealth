# OpenAI
export OPENAI_API_KEY="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"
export OPENAI_API_BASE=""
# Wenxin
export WENXIN_API_KEY=""
export WENXIN_SECRET_KEY=""
# Qwen
export DASHSCOPE_API_KEY=""
export DASHSCOPE_API_KEY=""


python run.py \
    --scenario Scenario.CollaborativeConsultation \
    --patient_database ./data/patients.json \
    --doctor_database ./data/collaborative_doctors/doctors.json \
    --patient Agent.Patient.GPT --patient_openai_model_name gpt-3.5-turbo \
    --reporter Agent.Reporter.GPT --reporter_openai_model_name gpt-3.5-turbo \
    --host Agent.Host.GPT --host_openai_model_name gpt-4 \
    --number_of_doctors 2 --max_discussion_turn 4 \
    --save_path outputs/collaboration_history_iiyi/doctors_2_agent_gpt3_gpt4_wenxin_parallel_with_critique_discussion_history_0222.jsonl \
    --discussion_mode Parallel_with_Critique # --parallel --max_workers 8

