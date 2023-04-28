from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route("/")
def homepage():
  return render_template("homepage.html",
                         src = "static",
                         eed="Homepage" ,
                         logo="logo",
                         cname="Eid Hamada",
                         co1_n = "شركة حمادة للسيراميك",co1_url ="hamada_ceramc.com",co1_img="273264708_5033452513334627_7766457200191709172_n.jpg",co1_text="لقد قامت شركة عيد حمادة البرمجية بانشاء موقع جميل ومتميز لنا بالوقت المحدد,شركة تستحق كل التقدير" ,
                         co2_n = "شركة لاين فود صابحة",co2_url ="linefoof.com",co2_img="273147720_1779986005528716_5218920396414895359_n.jpg",co2_text="من افضل الشركات البرمجية التي تعاملنا معها شفافية ومصدقية كاملة ",
                         co3_n = "شركة شكشوكة للاحذية",co3_url ="sacsoka.com",co3_img="263720011_292873086180219_3473431983066555187_n.jpg",co3_text="لقد توسعنا بشكل كبير وواضح من بعد انشاء موقع الكتروني , لقد ساعدنا ذالك بشكل كبير لتوسعت اعمالنا وتكبيرها",
                         co4_n = "شركة الهيثم للدعاية والاعلان",co4_url ="alhytamforad.net",co4_img="102760734_1915261468608040_4740665280547530586_n.png",co4_text="لقد ساعدنا عمل حمل ترويجي عبر الرسائل بشكل كبير بمساعدة شركة حمادة البرمجية ,شركة تستحق كل التقدير",
                         co5_n = "شركة ومجموعة تاج هوم",co5_url ="taghome.groub",co5_img="243373709_396096015309253_7705805687276325116_n.jpg",co5_text="سعر غير معقول مع خدمات ممتاز ,كل الشكر والتقدير لشركة عيد حمادة البرمجية",                         
                         )

@skills_app.route("/about")
def about():
  return "About Page From Flask Framework"

if __name__ == "__main__":
  skills_app.run(debug=True, port=9000)
