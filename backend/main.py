
from fastapi import FastAPI, Body, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import and_
import uvicorn
from init import *
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def getUserIdByName(name):
    res = db.query(owner).filter(owner.name == name).first()
    if res is None : return 0
    return res.id

@app.get("/getUsers/{user}")
async def get_users(user):
    res = db.query(owner).all()
    users = [{'id': i.id, 'name': i.name} for i in res]
    id = 0
    for i in res:
        if i.name == user:
            id = i.id
            break
    return {'tableData': users, 'meid': id}

@app.get("/getUserInfo/{user}")
async def get_user_info(user):
    res = db.query(owner).filter(owner.name == user).first()
    return {'userInfo': res}

@app.get("/login,{name},{pwd}")
async def login(name, pwd):
    result = db.query(owner).filter(owner.name == name, owner.pwd == pwd).first()
    ret = {'can': False if result is None else True}
    if ret['can'] == True: ret['id'] = result.id
    return ret

@app.post("/register,{name},{pwd}")
async def register(name, pwd):
    res = db.query(owner).filter(owner.name == name).first()
    if res is not None:
        return {'can': False}
    user = owner(name=name, pwd=pwd, gender='男', age='18')
    db.add(user)
    db.commit()
    db.refresh(user)
    return {'can': True}

@app.get("/getecycle/{id}")
async def get_ecycle(id):
    res = db.query(ecycle).filter(ecycle.id == id).first()
    iu = db.query(battery).filter(battery.curECycleId == res.id).first() is not None
    res.btid = str(db.query(battery).filter(battery.curECycleId == res.id).first().id) if iu else 0
    return {'tableData': res}

@app.get("/ecycle/{user}")
async def get_ecycle(user):
    if(user == 'admin'):
        res = db.query(ecycle).all()
    else:
        id = getUserIdByName(user)
        print('id=',id)
        res = db.query(ecycle).filter(ecycle.ownerId == id).all()
    for i in res:
        i.ownerName = db.query(owner).filter(owner.id == i.ownerId).first().name
        iu = db.query(battery).filter(battery.curECycleId == i.id).first() is not None
        i.isUsing = '是' if iu else '否'
        i.BatteryId = str(db.query(battery).filter(battery.curECycleId == i.id).first().id) if iu else 0
    return {'tableData': res}

@app.post("/editECycle/{id}")
async def edit_ecycle(id:int, request: Request):
    data = await request.json()
    ec = db.query(ecycle).filter(ecycle.id == id).first()
    ec.type = data['type']
    ec.parameter = data['parameter']
    ec.ownerId = data['ownerId']
    db.commit()
    db.refresh(ec)
    return {'done': True}

@app.post("/addECycle")
async def edit_ecycle(request: Request):
    data = await request.json()
    ec = ecycle(type=data['type'], parameter=data['parameter'], ownerId=data['ownerId'])
    db.add(ec)
    db.commit()
    db.refresh(ec)
    return {'done': True}

@app.post("/deleteECycle/{id}")
async def delete_ecycle(id:int):
    ec = db.query(ecycle).filter(ecycle.id == id).first()
    db.delete(ec)
    db.commit()
    return {'done': True}

@app.post("/workorder/addworkorder")
async def add_workorder(request: Request):
    data = await request.json()
    wo = workorder(title=data['title'], content=data['content'], ownerId=data['ownerId'])
    db.add(wo)
    db.commit()
    db.refresh(wo)
    return {'done': True}

@app.get("/workorder/getallworkorder/{user}")
async def get_all_workorder(user):
    if(user == 'admin'):
        res = db.query(workorder).all()
    else:
        id = getUserIdByName(user)
        res = db.query(workorder).filter(workorder.ownerId == id).all()
    for i in res:
        i.ownerName = db.query(owner).filter(owner.id == i.ownerId).first().name
    return {'tableData': res}

@app.post("/workorder/deleteworkorder/{id}")
async def delete_workorder(id:int):
    wo = db.query(workorder).filter(workorder.id == id).first()
    db.delete(wo)
    db.commit()
    return {'done': True}

@app.get("/battery/getallbattery")
async def get_all_battery():
    res = db.query(battery).all()
    for i in res:
        if i.masterSlotId is not None:
            st = db.query(slot).filter(slot.id == i.masterSlotId).first()
            c = db.query(cabinet).filter(cabinet.id == st.masterId).first()
            i.curpos = str(st.id) + '-' + c.name + '-' + st.type
            i.cmasterid = c.id
        elif i.curECycleId is not None:
            i.curpos = '电车-' + str(db.query(ecycle).filter(ecycle.id == i.curECycleId).first().id)
        else:
            i.curpos = '未装配'
    return {'tableData': res}

@app.post("/battery/addbattery")
async def add_battery(request: Request):
    data = await request.json()
    bt = battery(size=data['size'], powerLeft=data['powerLeft'], status='待装配', masterSlotId=data['masterSlotId'], curECycleId=None)
    db.add(bt)
    db.commit()
    db.refresh(bt)
    return {'done': True}

@app.post("/battery/editbattery/{id}")
async def edit_battery(id:int, request: Request):
    data = await request.json()
    bt = db.query(battery).filter(battery.id == id).first()
    bt.size = data['size']
    bt.powerLeft = data['powerLeft']
    bt.status = data['status']
    bt.masterSlotId = data['masterSlotId']
    curECycleId=None
    db.commit()
    db.refresh(bt)
    return {'done': True}

@app.post("/battery/deletebattery/{id}")
async def delete_battery(id:int):
    bt = db.query(battery).filter(battery.id == id).first()
    db.delete(bt)
    db.commit()
    return {'done': True}

@app.post("/battery/link,{id},{cycleid}")
async def link_battery(id:int, cycleid:int):
    bt = db.query(battery).filter(battery.id == id).first()
    bt.curECycleId = cycleid
    bt.masterSlotId = None
    bt.status = '已装配'
    db.commit()
    db.refresh(bt)
    return {'done': True}

@app.post("/battery/unlink,{id},{masterSlotId}")
async def unlink_battery(id:int, masterSlotId:int):
    bt = db.query(battery).filter(battery.id == id).first()
    bt.curECycleId = None
    bt.masterSlotId = masterSlotId
    bt.status = '待装配'
    db.commit()
    db.refresh(bt)
    return {'done': True}

@app.get("/battery/battery/{id}")
async def get_battery(id:int):
    bt = db.query(battery).filter(battery.id == id).first()
    return {'battery': bt}

@app.get("/battery/getslotbattery/{id}")
async def get_slot_battery(id:int):
    bt = db.query(battery).filter(battery.masterSlotId == id).all()
    return {'tableData': bt}

@app.get("/cabinet/cabinet/{id}")
async def get_cabinet(id:int):
    cb = db.query(cabinet).filter(cabinet.id == id).first()
    return {'cabinet': cb}

@app.get("/cabinet/getallcabinet")
async def get_all_cabinet():
    res = db.query(cabinet).all()
    for i in res:
        i.companyName = db.query(company).filter(company.id == i.companyId).first().name
    return {'tableData': res}

@app.post("/cabinet/addcabinet")
async def add_cabinet(request: Request):
    data = await request.json()
    cb = cabinet(name=data['name'] ,pos=data['pos'], type=data['type'], maxSlotNum=data['maxSlotNum'],companyId=data['companyId'], locx=data['locx'], locy=data['locy'])
    db.add(cb)
    db.commit()
    db.refresh(cb)
    return {'done': True}

@app.post("/cabinet/editcabinet/{id}")
async def edit_cabinet(id:int, request: Request):
    cb = db.query(cabinet).filter(cabinet.id == id).first()
    data = await request.json()
    cb.name = data['name']
    cb.pos = data['pos']
    cb.type = data['type']
    cb.maxSlotNum = data['maxSlotNum']
    cb.companyId = data['companyId']
    cb.locx = data['locx']
    cb.locy = data['locy']
    db.commit()
    db.refresh(cb)
    return {'done': True}

@app.post("/cabinet/deletecabinet/{id}")
async def delete_cabinet(id:int):
    cb = db.query(cabinet).filter(cabinet.id == id).first()
    db.delete(cb)
    db.commit()
    return {'done': True}

@app.get("/company/company/{id}")
async def get_company(id:int):
    cp = db.query(company).filter(company.id == id).first()
    return {'company': cp}

@app.get("/company/getallcompany")
async def get_all_company():
    res = db.query(company).all()
    return {'tableData': res}

@app.post("/company/addcompany")
async def add_company(request: Request):
    data = await request.json()
    cp = company(name=data['name'], address=data['address'])
    db.add(cp)
    db.commit()
    db.refresh(cp)
    return {'done': True}

@app.post("/company/editcompany/{id}")
async def edit_company(id:int, request: Request):
    cp = db.query(company).filter(company.id == id).first()
    data = await request.json()
    cp.name = data['name']
    cp.address = data['address']
    db.commit()
    db.refresh(cp)
    return {'done': True}

@app.post("/company/deletecompany/{id}")
async def delete_company(id:int):
    cp = db.query(company).filter(company.id == id).first()
    db.delete(cp)
    db.commit()
    return {'done': True}

@app.get("/slot/getallslot")
async def get_all_slot():
    res = db.query(slot).all()
    for i in res:
        i.usedNum = db.query(battery).filter(battery.masterSlotId == i.id).count()
        i.pos = db.query(cabinet).filter(cabinet.id == i.masterId).first().pos
        i.masterName = db.query(cabinet).filter(cabinet.id == i.masterId).first().name
        i.name = str(i.id) + '-' + i.masterName + '-' + i.type
    return {'tableData': res}

@app.get("/slot/slot/{id}")
async def get_slot(id:int):
    sl = db.query(slot).filter(slot.id == id).first()
    sl.name = str(sl.id) + db.query(cabinet).filter(cabinet.id == sl.masterId).first().name + '-' + sl.type
    return {'slot': sl}

@app.post("/slot/addslot")
async def add_slot(request: Request):
    data = await request.json()
    sl = slot(masterId=data['masterId'], maxNum=data['maxNum'], type=data['type'])
    db.add(sl)
    db.commit()
    db.refresh(sl)
    return {'done': True}

@app.post("/slot/editslot/{id}")
async def edit_slot(id:int, request: Request):
    sl = db.query(slot).filter(slot.id == id).first()
    data = await request.json()
    sl.masterId = data['masterId']
    sl.maxNum = data['maxNum']
    sl.type = data['type']
    db.commit()
    db.refresh(sl)
    return {'done': True}

@app.post("/slot/deleteslot/{id}")
async def delete_slot(id:int):
    sl = db.query(slot).filter(slot.id == id).first()
    db.delete(sl)
    db.commit()
    return {'done': True}

@app.get("/slot/getcabinetslot/{id}")
async def get_cabinet_slot(id:int):
    res = db.query(slot).filter(slot.masterId == id).all()
    for i in res:
        i.usedNum = db.query(battery).filter(battery.masterSlotId == i.id).count()
    return {'tableData': res}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5555)