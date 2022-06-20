//Манипуляции
function manipulation_add() {
    let tbody = document.getElementById('manipulation_table').querySelector('tbody')
    let count = tbody.childNodes
    if (count.length == 0) {
        var n = 0
    }
    else {
        var n = count.length
    }
    let tr = document.createElement('tr')
    tr.setAttribute("n", n)
    let manipulation = ['datm', 'tnvr', 'tnvr_fam', 'kodmn', 'kodmn_naim', 'kol', 'pl', 'btn']
    for (let i = 0; i < manipulation.length; i++) {
        let td = document.createElement('td')
        td.setAttribute('name', manipulation[i])
        td.setAttribute("tr", n)
        if (manipulation[i] == "pl"){
            let select = document.createElement("select")
            select.setAttribute('name', manipulation[i])
            select.setAttribute("tr", n)
                select.classList.add('custom-select')
                select.classList.add('text-center')
                let pl = ['Неизвестно', 'Да', 'Нет']
                for (let i = 0; i < pl.length; i++) {
                    let option = document.createElement("option")
                    option.innerText = pl[i]
                    select.appendChild(option)
                }
                select.value = ''
                td.appendChild(select)
        }
        else if ((manipulation[i] == "btn")){
            // let btn = document.createElement("input")
            // btn.setAttribute('type', 'button')
            // btn.classList.add('btn')
            // btn.classList.add('btn-danger')
            // btn.value = 'Удалить'
            // btn.addEventListener("click", function () {
            //     tr.remove()
            //     Manipulation_delete(td)
            // })
            // td.appendChild(btn)
        }
        else{
            let ed = document.createElement("input")

            if (manipulation[i] == 'datm'){
                ed.setAttribute("style", "width:100px")
            }
            else if  (manipulation[i] == 'tnvr'){
                ed.setAttribute("style", "width:100px")
            }
            else if  (manipulation[i] == 'tnvr_fam'){
                ed.setAttribute("style", "width:180px")
            }
            else if  (manipulation[i] == 'kodmn'){
                ed.setAttribute("style", "width:100px")
            }
            else if  (manipulation[i] == 'kodmn_naim'){
                ed.setAttribute("style", "width:210px")
            }
            else if  (manipulation[i] == 'kol'){
                ed.setAttribute("style", "width:60px")
            }

            ed.setAttribute('name', manipulation[i])
            ed.setAttribute("tr", n)
            td.appendChild(ed)
        }
  
        tr.appendChild(td)
    }
    tbody.appendChild(tr)
    obj = {}
    for (let t = 0; t < tr.childNodes.length; t++) {
        let td = tr.childNodes[t]
        if (td.getAttribute("name") != "btn") {
            obj[td.getAttribute("name")] = ''
        }
        
    }
    app.$data.history.manipulation.push(obj)
    // Manipulation_click_edit()
    Manipulation_input()
}

function Manipulation_edit() {
    let tbody = document.getElementById("inf_manipulation").querySelector("tbody")
    tbody.innerHTML = ""
    let v_manipulation = app.$data.history.manipulation
    var n = 0
    for (let manipulations in v_manipulation) {
        let tr = document.createElement("tr")
        tr.setAttribute("n", n)
        let manipulation = v_manipulation[manipulations]
        for (let man in manipulation) {
            let td = document.createElement("td")
            td.setAttribute("name", man)
            td.setAttribute("tr", n)
            if (man == "pl") {
                let select = document.createElement("select")
                select.setAttribute("name", man)
                select.setAttribute("tr", n)
                select.classList.add('custom-select')
                select.classList.add('text-center')
                let pl = ['Неизвестно', 'Да', 'Нет']
                for (let i = 0; i < pl.length; i++) {
                    let option = document.createElement("option")
                    option.innerText = pl[i]
                    select.appendChild(option)
                }
                select.value = manipulation[man]
                td.appendChild(select)
            }
            else {
                let ed = document.createElement("input")

                if (man == 'datm'){
                    ed.setAttribute("style", "width:100px")
                }
                else if  (man == 'tnvr'){
                    ed.setAttribute("style", "width:100px")
                }
                else if  (man == 'tnvr_fam'){
                    ed.setAttribute("style", "width:180px")
                }
                else if  (man == 'kodmn'){
                    ed.setAttribute("style", "width:100px")
                }
                else if  (man == 'kodmn_naim'){
                    ed.setAttribute("style", "width:210px")
                }
                else if  (man == 'kol'){
                    ed.setAttribute("style", "width:60px")
                }

                ed.setAttribute("name", man)
                ed.setAttribute("tr", n)
                ed.value = manipulation[man]
                td.appendChild(ed)
            }
            tr.appendChild(td)
        }

        // let td = document.createElement("td")
        // td.setAttribute("name", "btn")
        // let btn = document.createElement("input")
        // btn.setAttribute('type', 'button')
        // btn.classList.add('btn')
        // btn.classList.add('btn-danger')
        // btn.value = 'Удалить'

        // btn.addEventListener("click", function () {
        //     tr.remove()
        //     Manipulation_delete(td)
        // })
        // td.appendChild(btn)
        // td.setAttribute("tr", n)
        // tr.appendChild(td)

        tbody.appendChild(tr)
        n += 1
    }
    Manipulation_input()
// Manipulation_click_edit()
}

function Manipulation_input(){
    let kod_vra = app.$data.sprav_list.Vra
    let str_vra = ''
    for (let k = 0; k < kod_vra.length; k++) {
        str_vra += '<option value="' + kod_vra[k].kod + '" />'
    }
    let kodmn = app.$data.sprav_list.AbObsh
    let str_kodmn = ''
    for (let k = 0; k < kodmn.length; k++) {
        str_kodmn += '<option value="' + kodmn[k].kod + '" />'
    }
    var table = document.getElementById("manipulation_table")
    var cells = table.getElementsByTagName("td")
    for (let i = 0; i < cells.length; i++) {
        if ((cells[i].getAttribute("name") == "datm") || (cells[i].getAttribute("name") == "tnvr") || (cells[i].getAttribute("name") == "kodmn")){
            let input = cells[i].childNodes[0] 
            if (cells[i].getAttribute("name") == "datm"){
                input.setAttribute("maxlength",8)
                input.addEventListener("input",function(){
                    var n = input.value.replace(/[^0-9]/g,'').split('')
                    if(n.length > 2) n.splice(2,0,'-');
                    if(n.length > 4) n.splice(5,0,'-');
                    input.value = n.join('');
                })
                input.addEventListener("change",function(){
                    Manipulation_update(cells[i])
                })
            }

            if (cells[i].getAttribute("name") == "tnvr") {
                let data = document.createElement("datalist")
                data.setAttribute('id', cells[i].getAttribute('name'))
                data.innerHTML = str_vra
                input.setAttribute('list', cells[i].getAttribute('name'))
                cells[i].append(data)
                input.addEventListener('change', function () {
                  let query = `
                          query{
                              VraName(kod:"${input.value}"){
                                naim
                              }
                          }`
                  fetch('graph_hospital/', {
                      method: 'post',
                      headers: {
                        'Content-Type': 'application/json',
                      },
                      body: JSON.stringify({query})
                    })
                    .then(response => response.json())
                    .then(data => {
                            var tr_list = document.getElementById("manipulation_table").querySelector("tbody").querySelectorAll("tr")
                            var tr = tr_list[cells[i].getAttribute("tr")]
                            var naim = tr.childNodes[2]
                            naim.childNodes[0].value = data.data.VraName[0].naim
                            Manipulation_update(tr.childNodes[1])
                            Manipulation_update(tr.childNodes[2])
                    })
                    .catch((e) => {
                      // console.log(e)
                    })
                })
            }
            else if (cells[i].getAttribute("name") == "kodmn"){
                let data = document.createElement("datalist")
                data.setAttribute('id', cells[i].getAttribute('name'))
                data.innerHTML = str_kodmn
                input.setAttribute('list', cells[i].getAttribute('name'))
                cells[i].append(data)

                input.addEventListener('change', function () {

                  let query = `
                          query{
                              AbObshName(kod:"${input.value}"){
                                ima
                              }
                          }`
                  fetch('graph_hospital/', {
                      method: 'post',
                      headers: {
                        'Content-Type': 'application/json',
                      },
                      body: JSON.stringify({query})
                    })
                    .then(response => response.json())
                    .then(data => {
                            var tr_list = document.getElementById("manipulation_table").querySelector("tbody").querySelectorAll("tr")
                            var tr = tr_list[cells[i].getAttribute("tr")]
                            var naim = tr.childNodes[4]
                            naim.childNodes[0].value = data.data.AbObshName[0].ima
                            Manipulation_update(tr.childNodes[3])
                            Manipulation_update(tr.childNodes[4])
                    })
                    .catch((e) => {
                      // console.log(e)
                    })
                })
            }
           

        }
        else{
            if (cells[i].getAttribute("name") == "kol")
            {
                let input = cells[i].childNodes[0] 
                input.addEventListener("change",function(){
                    Manipulation_update(cells[i])
                })
            }
        }
    }
}

function Manipulation_update(td) {
    let v_manipulation = app.$data.history.manipulation
    if (td.getAttribute("name") == "pl"){
        v_manipulation[td.getAttribute("tr")][td.getAttribute("name")] = td.childNodes[0].value
    }
    else{
        v_manipulation[td.getAttribute("tr")][td.getAttribute("name")] = td.childNodes[0].value
    }
}
function Manipulation_delete(td) {
    let v_manipulation = app.$data.history.manipulation
    let manipulation = []

    for (let m = 0; m < v_manipulation.length; m++) {
        if (m != td.getAttribute("tr")) {
            manipulation.push(v_manipulation[m])
        }
    }
    app.$data.history.manipulation = manipulation
    Manipulation_edit()
    Manipulation_input()
}