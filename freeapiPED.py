import requests
import bs4
from requests_toolbelt import MultipartEncoder
class Freeapi():
    def __init__(self) -> None:

        self.URI = "http://www.acimed.sld.cu/"
        self.host = "www.acimed.sld.cu"
        self.username = "titilm30"

        self.password = "TitiLM30*"

        

        self.Session = requests.Session()

        self.login()

        pass

    def login(self):

        data = {"source":"","username": self.username ,"password": self.password}

        self.Session.headers.update({"Content-Type":"application/x-www-form-urlencoded"})

        respuesta = self.Session.post(url="http://"+self.host+"/index.php/acimed/login/signIn",data=data)

        

        pass
    def getarticleId(self):

        self.Session.headers.update({"Content-Type":"application/x-www-form-urlencoded"})

        data = {
         "submissionChecklist": "1",
         "sectionId":"1",
         "locale": "es_ES",
         "checklist":["1","2","3","4","5"],
         'copyrightNoticeAgree': "1",
        'co mmentsToEditor': ""
           }

        respano =  self.Session.post("http://"+self.host+"/index.php/acimed/author/saveSubmit/1",data=data)
        
        respa = self.Session.get(url=respano.url)

        self.URI = respano.url
        
        soup = bs4.BeautifulSoup(respa.text,'html.parser')

        query = soup.find('input',attrs={'name':'articleId','type':'hidden'})['value']

        return query
        pass
    def upload_file(self,filepath):
           
           articleID = self.getarticleId()

           submitnumber = self.URI.split('/')[-1].split("?")[0]

           datospaso2 ={
               'articleId':articleID,
               'submissionFile':("","","application/octet-stream")

           }

           f= MultipartEncoder(fields=datospaso2)

           cabeceras = {"Content-Type":f.content_type}

           paso2 = self.Session.post(url="http://"+self.host+"/index.php/acimed/author/saveSubmit/"+submitnumber,data=f,headers=cabeceras)
                    
           datas ="articleId="+articleID+"&formLocale=es_ES&deletedAuthors=&moveAuthor=0&moveAuthorDir=&moveAuthorIndex=&authors%5B0%5D%5BauthorId%5D=6133&authors%5B0%5D%5Bseq%5D=1&primaryContact=0&authors%5B0%5D%5BfirstName%5D=Alberto&authors%5B0%5D%5BmiddleName%5D=&authors%5B0%5D%5BlastName%5D=Alfonso+Perez&authors%5B0%5D%5Bemail%5D=axinotelegram%40gmail.com&authors%5B0%5D%5Borcid%5D=&authors%5B0%5D%5Burl%5D=&authors%5B0%5D%5Baffiliation%5D%5Bes_ES%5D=&authors%5B0%5D%5Bcountry%5D=&authors%5B0%5D%5BcompetingInterests%5D%5Bes_ES%5D=&authors%5B0%5D%5Bbiography%5D%5Bes_ES%5D=&title%5Bes_ES%5D=test&abstract%5Bes_ES%5D=ddd&subject%5Bes_ES%5D=&language=es&sponsor%5Bes_ES%5D="
          
           paso3 = self.Session.post(url="http://"+self.host+"/index.php/acimed/author/saveSubmit/"+str(int(submitnumber)+1),data=datas)
           
                  
           namessplit = filepath.split('/')

           dataaa = {
               'articleId' : articleID,
               'uploadSuppFile':(namessplit[len(namessplit)-1],open(filepath,'rb'),"application/octet-stream"),
               'submitUploadSuppFile' :"Cargar"}
   


           e = MultipartEncoder(fields=dataaa)

           headers = {"Content-Type": e.content_type}

           daticos = self.Session.get(url=paso3.url)

           soupa  = bs4.BeautifulSoup(daticos.text ,'html.parser')

           sacado = soupa.find('form',attrs={"enctype":"multipart/form-data"})

           sacadp = sacado.attrs.get("action")


           respuesta = self.Session.post(url=sacadp,data=e,headers=headers)



           paso4pet = self.Session.get(url=respuesta.url)

           soupa  = bs4.BeautifulSoup(paso4pet.text ,'html.parser')

           sacado = soupa.find("form",attrs={"enctype":"multipart/form-data"})

           datospaso4 ={
               "articleId":articleID,
               "fromLocale":"es_ES",
               "title[es_ES]":"sin titulo",
               "creator[es_ES]":"",
               "subject[es_ES]":"",
               "type":"Herramienta de investigación",
               "typeOther[es_ES]":"",
               "description[es_ES]":"",
               "publisher[es_ES]":"",
               "sponsor[es_ES]":"",
               "dateCreated":"2022-10-22",
               "source[es_ES]":"",
               "language":"",
               "uploadSuppFile":("","","application/octet-stream")

           }
           paso4meul = MultipartEncoder(fields=datospaso4)
           
           headers = {"Content-Type":paso4meul.content_type}

           paso4post = self.Session.post(url=sacado.get("action"),data=paso4meul,headers=headers)
          
           datapaso5 = {
               "articleId":articleID,
               "uploadSuppFile":("","","application/octet-stream")
               
           }

           datosm5paso = MultipartEncoder(fields=datapaso5)

           headers={"Content-Type":datosm5paso.content_type}

           paso5 = self.Session.post(url=sacadp,data=datosm5paso,headers=headers)

           urlfile = self.Session.get(url=paso5.url)

           soupera = bs4.BeautifulSoup(urlfile.text ,'html.parser')

           sacadolink = soupera.find("a",attrs={"class":"file"})

           self.Session.headers.update({"Content-Type":"application/x-www-form-urlencoded"})

           datosfinal = {
               "articleId":articleID
           }
           subnumber = paso5.url.split("?")[0]

           finalnumber = subnumber.split("/")

           finalizar = self.Session.post(url="http://"+self.host+"/index.php/acimed/author/saveSubmit/"+finalnumber[len(finalnumber)-1],data=datosfinal)

           print(finalizar.url)
           
           return sacadolink.attrs.get("href")
    pass
