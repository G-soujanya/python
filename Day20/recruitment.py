#lex_auth_012751878508396544244
#Start writing your code here
class Applicant:
    __application_dict={"A":0,"B":0,"C":0}
    __applicant_id_count=1000 
    def __init__(self,applicant_name):
        self.__applicant_name=applicant_name 
        self.__applicant_id=0 
        self.__job_band=None
    def generate_applicant_id(self):
        self.__applicant_id=Applicant.__applicant_id_count+1
        Applicant.__applicant_id_count+=1
    def apply_for_job(self,job_band):
        for key,value in Applicant.__application_dict.items():
            if(key==job_band):
                if(value<5):
                    Applicant.__application_dict[key]+=1 
                    self.generate_applicant_id()
                    self.__job_band=job_band 
                else:
                    return -1
    @staticmethod
    def get_application_dict():
        return __application_dict 
    def get_applicant_id(self):
        return self.__applicant_id
    def get_job_band(self):
        return self.__job_band 
    def get_applicant_name(self):
        return self.__applicant_name
a=Applicant("nithya")
if(a.apply_for_job("A")):
    print(a.get_applicant_id())
    print(a.get_applicant_name())
    print(a.get_job_band())
else:
    print("Not a valid job band or application process is completed")
