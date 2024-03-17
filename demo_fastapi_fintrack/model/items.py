# model/items.py
from fastapi import Depends, HTTPException, APIRouter, Form
from .db import get_db

ItemsRouter = APIRouter(tags=["Items"])

@ItemsRouter.get("/Items", response_model=list)
async def read_Items(
    db=Depends(get_db)
):
    query= "SELECT ItemID, ItemName, FromLab, ItemDescription FROM item"
    db[0].execute(query)
    Items = [{"ItemID": Items[0], "ItemName": Items[1], "FromLab": Items[2], "ItemDescription": Items[3]} for Items in db[0].fetchall()]
    return Items

@ItemsRouter.get("/Items/{ItemID}", response_model=dict)
async def read_Item(
    ItemID: str,
    db=Depends(get_db)
):
    query = "SELECT ItemID, ItemName,FromLab, ItemDescription FROM item WHERE ItemID = %s"
    db[0].execute(query, (ItemID,))
    Item = db[0].fetchone()
    
    if Item:
        return{
        "ItemID": Item[0],
        "ItemName": Item[1],
        "FromLab": Item[2],
        "ItemDescription": Item[3],
        }
    raise HTTPException(status_code=404, detail="Item not found")

@ItemsRouter.post("/Items",response_model=dict)
async def create_Item(
     ItemName: str = Form(...),
     FromLab: str = Form(...),
     ItemDescription: str = Form(...),
     db=Depends(get_db)
):
    query="INSERT INTO item ( ItemName, FromLab, ItemDescription) VALUES (%s,%s,%s) "
    db[0].execute(query, (ItemName,FromLab,ItemDescription)) 
    db[1].commit()

    db[0].execute("SELECT LAST_INSERT_ID()")
    new_item_id = db[0].fetchone()[0]
    db[1].commit()

    return{
              "ItemName": ItemName,
              "FromLab": FromLab,
              "ItemDescription": ItemDescription,
    }

@ItemsRouter.put("/Items/{Item}", response_model=dict)
async def update_Item( 
     ItemID: str = Form(...),
     ItemName: str = Form(...),
     FromLab: str = Form(...),
     ItemDescription: str = Form(...),
     db=Depends(get_db)
):
    query = "UPDATE item SET ItemName = %s, FromLab = %s, ItemDescription = %s WHERE ItemID = %s"
    db[0].execute(query,(ItemName,FromLab,ItemDescription, ItemID,))
    
    if db[0].rowcount > 0 :
        db[1].commit()
        return{"message": "Item Updated Successfully"}
    
    raise HTTPException(status_code=404, detail="Item not found")

@ItemsRouter.delete("Items/{Item}", response_model=dict)
async def delete_Item(
     ItemID: int = Form(...),
     db=Depends(get_db)
): 
    try:
        query_check_Item = "SELECT ItemID from item WHERE ItemID = %s"
        db[0].execute(query_check_Item,(ItemID,))
        existing_Item= db[0].fetchone()
        
        if not existing_Item:
            raise HTTPException(status_code=404, detail="Category not found")
        
        query_delete_Item = "DELETE FROM item WHERE ItemID = %s"
        db[0].execute(query_delete_Item, (ItemID,))
        db[1].commit()
        
        return{"message": "Item Deleted Successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
    finally:
        db[0].close()