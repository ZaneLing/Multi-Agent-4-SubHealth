from .base_agent import Agent
from utils.register import register_class, registry

@register_class(alias="Agent.Patient.GPT")
class Patient(Agent):
    def __init__(self, args, patient_profile, medical_records, patient_id=0):
        engine = registry.get_class("Engine.GPT")(
            openai_api_key=args.patient_openai_api_key, 
            openai_api_base=args.patient_openai_api_base,
            openai_model_name=args.patient_openai_model_name, 
            temperature=args.patient_temperature, 
            max_tokens=args.patient_max_tokens,
            top_p=args.patient_top_p,
            frequency_penalty=args.patient_frequency_penalty,
            presence_penalty=args.patient_presence_penalty
        )

        self.system_message = "You're a resident. This is your basic information\n" + \
            "{}\n".format(patient_profile)
        self.system_message += "< degree of obesity >{}\n".format(patient_profile["NObeyesdad"])
        self.system_message += "\n"
        
        if(patient_profile["score"] < 70):
            self.system_message += "Your physical health score is below 70 points, and you are in a sub-health state. You need to get help from a doctor.\n"
            self.system_message += \
                "There will be < doctor > below to diagnose your medical condition, you need:\n" + \
                "(1) Dialogue according to the basic information.\n" + \
                "(2) First you have to tell doctor your degree of obesity.\n" + \
                "(3) When the doctor asks you about your information, respond according to the relevant content. \n" + \
                "(4) Keep your answers colloquial and as short as possible, providing the most important information.\n" + \
                "(5) When the doctor gives the diagnosis, the corresponding diagnosis basis and treatment plan, add the special character < end > at the end of the dialogue"

        @staticmethod
        def add_parser_args(parser):
            # group = parser.add_argument_group('Agent.Patient.GPT Arguments')
            parser.add_argument('--patient_openai_api_key', type=str, help='API key for OpenAI')
            parser.add_argument('--patient_openai_api_base', type=str, help='API base for OpenAI')
            parser.add_argument('--patient_openai_model_name', type=str, help='API model name for OpenAI')
            parser.add_argument('--patient_temperature', type=float, default=0.0, help='temperature')
            parser.add_argument('--patient_max_tokens', type=int, default=2048, help='max tokens')
            parser.add_argument('--patient_top_p', type=float, default=1, help='top p')
            parser.add_argument('--patient_frequency_penalty', type=float, default=0, help='frequency penalty')
            parser.add_argument('--patient_presence_penalty', type=float, default=0, help='presence penalty')

        def speak(self, role, content, save_to_memory=True):
            messages = [{"role": memory[0], "content": memory[1]} for memory in self.memories]
            messages.append({"role": "user", "content": f"<{role}> {content}"})

            responese = self.engine.get_response(messages)
            
            if save_to_memory:
                self.memorize(("user", f"<{role}> {content}"))
                self.memorize(("assistant", responese))

            return responese
    
        @staticmethod
        def parse_role_content(responese):
            responese = responese.strip()

            speak_to = "医生"

            return speak_to, responese