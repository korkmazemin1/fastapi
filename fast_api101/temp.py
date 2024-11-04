from fastapi import FastAPI,HTTPException
# HTTPExpecteions hataları göstermek için kullanılack fonksiyondur
from pydantic import BaseModel
# fastapinin desteklediği  pydantic  ile server üzerindeki verileri düzenleyebilir yapıları ile oynayabiliriz

# fast api ile bir uygulama oluşturma
app=FastAPI()

class Item(BaseModel):
    text : str = None
    is_done : bool = False 

items=[]

# fastapi ile bir yol tanımladık
# buradaki yol çağrıldığında alt tarafta tanımlanan fonksiyon çalışacaktır
@app.get("/")
def root():
    return {"Merhaba":"Dunya"}


@app.post("/items")# bağlantıya ek bu yazılırsa aşağıdaki fonksiyona erişilecek
def create_item(item:Item):
    items.append(item)
    return items     


# bu işlemde items listesinin gösterilirken kaç tane eleman gösterileceğine dair default bir sınıf verildi 
# ek olarak get lerken bu default parametre değiştirilebilir 
@app.get("/items")
def list_items(limit: int =3 ):
    return items[0:limit]



@app.get("/items/{item_id}")# url yolu ile input alınıp bu get_item fonksiyonuna iletilir 

# get item fonksiyonu ile url de item/id şeklinde gelen id ile item listesindeki id ye göre o id items listesinden çekilir 
def get_item(item_id: int )-> Item:# bu şekilde bir kullanım ile item integer olarak alınan bir ifadenin string halinde kullanılması sağlanır veya yazıldığı gibi daha öncesinde tipi belirlenmiş olan Item nesnesine dönüştürebiliriz   
    if item_id< len(items):
        return items[item_id]    # item id ye göre listeden eleman seçilir
    else :
        raise HTTPException(status_code=404, detail=f"bunu mu ariyon kanka ? {item_id}  --------->>>>>>>>------->>>>>>>>       kalmamis bundan ")
    # üst taraftaki dönüşüm işlemi fastapi kütüphanesinin bir meyvesidir :)) 