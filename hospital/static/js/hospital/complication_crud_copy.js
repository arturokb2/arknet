function Complication_add() {
    let tbody = document.getElementById("complication_table").querySelector("tbody")

    let count = tbody.childNodes
    if (count.length == 0) {
        var n = 0
    }
    else {
        var n = count.length
    }
    let v_oper = app.$data.history.oper
    // console.log(v_oper)
    var select = document.createElement("select")
    select.classList.add('custom-select')
    select.classList.add('text-center')
    for (let opers in v_oper) {
        // console.log(v_oper[opers])
        let option = document.createElement("option")

        if (v_oper[opers]['pop'] == "Да"){
            option.innerText = v_oper[opers]['kod_op']
            select.appendChild(option)
        }
    }

    let tr = document.createElement("tr")
    tr.setAttribute("n", n)
    // let complication = ['inf_oper', 'tnvr', 'tnvr_fio', 'dato', 'osl', 'osl_naim', 'xosl', 'posl', 'aosl', 'btn']
    let complication = ['tnvr', 'tnvr_fio', 'dato', 'osl', 'osl_naim', 'xosl', 'posl', 'aosl', 'btn']

    for (let i = 0; i < complication.length; i++) {
        let td = document.createElement("td")
        td.setAttribute('name', complication[i])
        if (complication[i] == 'inf_oper') {
            select.value = ''
            select.setAttribute("name", complication[i])
            select.setAttribute("tr", n)
            td.appendChild(select)
            td.setAttribute("name", complication[i])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }
        else if (complication[i] == 'xosl') {
            let select = document.createElement("select")
            select.setAttribute("name", complication[i])
            select.setAttribute("tr", n)
            select.classList.add('custom-select')
            select.classList.add('text-center')
            // let xosl = ['при лечении', 'интрооперационное', 'послеоперационное', 'другое']
            let xosl = ['1', '2', '3', '4']
            for (let i = 0; i < xosl.length; i++) {
                let option = document.createElement("option")
                option.innerText = xosl[i]
                select.appendChild(option)
            }
            select.value = ''
            td.appendChild(select)

            td.setAttribute("tr", n)
            tr.appendChild(td)
        }
        else if (complication[i] == 'posl') {
            let select = document.createElement("select")
            select.setAttribute("name", complication[i])
            select.setAttribute("tr", n)
            select.classList.add('custom-select')
            select.classList.add('text-center')
            // let posl = ['из-за болезни', 'ятрогенная', 'тех.оснащение', 'другая']
            let posl = ['1', '2', '3', '4']
            for (let i = 0; i < posl.length; i++) {
                let option = document.createElement("option")
                option.innerText = posl[i]
                select.appendChild(option)
            }
            select.value = ''
            td.appendChild(select)
            td.setAttribute("name", complication[i])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }
        else if (complication[i] == 'aosl') {
            let select = document.createElement("select")
            select.setAttribute("name", complication[i])
            select.setAttribute("tr", n)
            select.classList.add('custom-select')
            select.classList.add('text-center')

            // let aosl = ['приведшеее к летальному исходу', 'опасное для жизни', 'удлиняющее пребывание', 'другое']
            let aosl = ['1', '2', '3', '4']
            for (let i = 0; i < aosl.length; i++) {
                let option = document.createElement("option")
                option.innerText = aosl[i]
                select.appendChild(option)
            }
            select.value = ''
            td.appendChild(select)
            td.setAttribute("name", complication[i])
            td.setAttribute("tr", n)
            tr.appendChild(td)
        }
        else if (complication[i] == 'btn') {
            // let btn = document.createElement("input")
            // btn.setAttribute('type', 'button')
            // btn.classList.add('btn')
            // btn.classList.add('btn-danger')
            // btn.value = 'Удалить'
            // btn.addEventListener("click", function () {
            //     tr.remove()
            // })
            // td.appendChild(btn)

        }


        else {
            td.setAttribute("tr", n)
            let ed = document.createElement("input")
            ed.setAttribute("name", complication[i])
            ed.setAttribute("tr", n)
            if (complication[i] == 'tnvr'){
                ed.setAttribute("style", "width:100px")
            }
            else if  (complication[i] == 'dato'){
                ed.setAttribute("style", "width:100px")
            }
            else if  (complication[i] == 'osl'){
                ed.setAttribute("style", "width:60px")
            }
            else if  (complication[i] == 'osl_naim'){
                ed.setAttribute("style", "width:260px")
            }

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
    app.$data.history.sl_oslo.push(obj)
    
    Complication_input()
}

function Complication_edit() {
    let tbody = document.getElementById("complication_table").querySelector("tbody")
    tbody.innerHTML = ""

    let v_complication = app.$data.history.oslo
    // console.log(v_complication)
    let v_oper = app.$data.history.oper
    var n = 0
    if (v_complication != ''){
        for (let complications in v_complication) {
            let tr = document.createElement("tr")
            tr.setAttribute("n", n)
            let complication = v_complication[complications]
            var select = document.createElement("select")
            select.classList.add('custom-select')
            select.classList.add('text-center')
            // for (let opers in v_oper) {
            //     let option = document.createElement("option")
    
        
                
            //     if (v_oper[opers]['pop'] == "Да"){
            //         option.innerText = v_oper[opers]['kod_op']
            //         select.appendChild(option)
            //     }
            // }
            for (let com in complication) {
    
                let td = document.createElement("td")
                if (com == "inf_oper") {
                 
                    // select.value = complication[com]
                    // select.setAttribute("name", com)
                    // select.setAttribute("tr", n)
                    // td.appendChild(select)
                    // td.setAttribute("name", com)
                    // td.setAttribute("tr", n)
                    // tr.appendChild(td)
    
                }
                else if (com == 'xosl') {
                   
                    let select = document.createElement("select")
                    select.setAttribute("name", com)
                    select.setAttribute("tr", n)
                    select.classList.add('custom-select')
                    select.classList.add('text-center')
                    // let xosl = ['при лечении', 'интрооперационное', 'послеоперационное', 'другое']
                    let xosl = ['1', '2', '3', '4']
                    for (let i = 0; i < xosl.length; i++) {
                        let option = document.createElement("option")
                        option.innerText = xosl[i]
                        select.appendChild(option)
                    }
                    select.value = complication[com]
                    td.appendChild(select)
                    td.setAttribute("name", com)
                    td.setAttribute("tr", n)
                    tr.appendChild(td)
                }
                else if (com == "posl") {
                    let select = document.createElement("select")
                    select.setAttribute("name", com)
                    select.setAttribute("tr", n)
                    select.classList.add('custom-select')
                    select.classList.add('text-center')
                    // let posl = ['из-за болезни', 'ятрогенная', 'тех.оснащение', 'другая']
                    let posl = ['1', '2', '3', '4']
                    for (let i = 0; i < posl.length; i++) {
                        let option = document.createElement("option")
                        option.innerText = posl[i]
                        select.appendChild(option)
                    }
                    select.value = complication[com]
                    td.appendChild(select)
                    td.setAttribute("name", com)
                    td.setAttribute("tr", n)
                    tr.appendChild(td)
                }
                else if (com == "aosl") {
                    let select = document.createElement("select")
                    select.setAttribute("name", com)
                    select.setAttribute("tr", n)
                    select.classList.add('custom-select')
                    select.classList.add('text-center')
                    // let aosl = ['приведшеее к летальному исходу', 'опасное для жизни', 'удлиняющее пребывание', 'другое']
                    let aosl = ['1', '2', '3', '4']
                    for (let i = 0; i < aosl.length; i++) {
                        let option = document.createElement("option")
                        option.innerText = aosl[i]
                        select.appendChild(option)
                    }
                    select.value = complication[com]
                    td.appendChild(select)
                    td.setAttribute("name", com)
                    td.setAttribute("tr", n)
                    tr.appendChild(td)
                }
                else {
                    // td.innerText = complication[com]
                    let ed = document.createElement("input")

                    if (com == 'tnvr'){
                        ed.setAttribute("style", "width:100px")
                    }
                    else if  (com == 'dato'){
                        ed.setAttribute("style", "width:100px")
                    }
                    else if  (com == 'osl'){
                        ed.setAttribute("style", "width:60px")
                    }
                    else if  (com == 'osl_naim'){
                        ed.setAttribute("style", "width:260px")
                    }

                    ed.setAttribute("name", com)
                    ed.setAttribute("tr", n)
                    ed.value = complication[com]
                    td.setAttribute("name", com)
                    td.setAttribute("tr", n)
                    td.appendChild(ed)
                    tr.appendChild(td)
                }
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
            //     Complication_delete(td)
            // })
            // td.appendChild(btn)
            // td.setAttribute("tr", n)
            // tr.appendChild(td)
    
            tbody.appendChild(tr)
            n += 1
        }
        Complication_input()
    }
    
}

function Complication_input() {
    let kod_vra = app.$data.sprav_list.Vra
    let str_vra = ''
    for (let k = 0; k < kod_vra.length; k++) {
        str_vra += '<option value="' + kod_vra[k].kod + '" />'
    }

    let kod_osl = app.$data.sprav_list.Pope
    let str_osl = ''
    for (let o = 0; o < kod_osl.length; o++) {
        str_osl += '<option value="' + kod_osl[o].kod + '" />'
    }

    var table = document.getElementById("complication_table")
    var cells = table.getElementsByTagName("td")

    for (let i = 0; i < cells.length; i++) {
        if ((cells[i].getAttribute("name") == "tnvr") || (cells[i].getAttribute("name") == "dato") || (cells[i].getAttribute("name") == "osl")) {
            let input = cells[i].childNodes[0]
            if (cells[i].getAttribute("name") == "dato") {
                input.setAttribute("maxlength", 8)
                input.addEventListener("input", function () {
                    var n = input.value.replace(/[^0-9]/g, '').split('')
                    if (n.length > 2) n.splice(2, 0, '-');
                    if (n.length > 4) n.splice(5, 0, '-');
                    input.value = n.join('');
                })
                // input.addEventListener('focus',function () {
                //         document.getElementById("inf_complication").scrollLeft = 100
                // })


                input.addEventListener('change', function () {
                    Complication_update(cells[i])
                })

            }
            else if (cells[i].getAttribute("name") == "tnvr"){
                let data = document.createElement("datalist")
                data.setAttribute('id', cells[i].getAttribute('name'))
                data.innerHTML = str_vra
                input.setAttribute('list', cells[i].getAttribute('name'))
                cells[i].append(data)
                // input.addEventListener('focus',function () {
                //         document.getElementById("inf_complication").scrollLeft = 200
                // })
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
                       var tr_list = document.getElementById("complication_table").querySelector("tbody").querySelectorAll("tr")
                            var tr = tr_list[cells[i].getAttribute("tr")]
                            var naim = tr.childNodes[2]
                            naim.childNodes[0].value = data.data.VraName[0].naim
                            // Complication_update(tr.childNodes[1])
                            // Complication_update(tr.childNodes[2])
                            Complication_update(tr.childNodes[0])
                            Complication_update(tr.childNodes[1])
                    })
                    .catch((e) => {
                      // console.log(e)
                    })

                })
            }

            else if (cells[i].getAttribute("name") == "osl") {
                let data = document.createElement("datalist")
                data.setAttribute('id', cells[i].getAttribute('name'))
                data.innerHTML = str_osl
                input.setAttribute('list', cells[i].getAttribute('name'))
                cells[i].append(data)
                var tr_list = document.getElementById("complication_table").querySelector("tbody").querySelectorAll("tr")
                var tr = tr_list[cells[i].getAttribute("tr")]
                input.addEventListener('focus',function () {
                        document.getElementById("inf_complication").scrollLeft = 800
                })
                input.addEventListener('change', function () {
                    if (input.value.trim().length > 0) {

                        let query = `
                                  query{
                                      PopeName(kod:"${input.value}"){
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
                            var tr_list = document.getElementById("complication_table").querySelector("tbody").querySelectorAll("tr")
                            var tr = tr_list[cells[i].getAttribute("tr")]
                            var naim = tr.childNodes[5]
                            naim.childNodes[0].value = data.data.PopeName[0].naim
                            // Complication_update(tr.childNodes[4])
                            // Complication_update(tr.childNodes[5])
                            Complication_update(tr.childNodes[3])
                            Complication_update(tr.childNodes[4])
                            })
                            .catch((e) => {
                              // console.log(e)
                            })



                    }
                    else {
                        // tr.childNodes[5].childNodes[0].value = ''
                        tr.childNodes[4].childNodes[0].value = ''
                    }

                })
            }
        }
        else{
            cells[i].onchange = function () {
                Complication_update(cells[i])
            }
        }
    }



}

function Complication_update(td) {
    let v_complication = app.$data.history.sl_oslo
    v_complication[td.getAttribute("tr")][td.getAttribute("name")] = td.childNodes[0].value
    // if ((td.getAttribute("name") == "tnvr") || (td.getAttribute("name") == "tnvr_fio") || (td.getAttribute("name") == "tnvr_fio")
    //     || (td.getAttribute("name") == "dato") || (td.getAttribute("name") == "osl") || (td.getAttribute("name") == "osl_naim")) {
    //     let tr_list = document.getElementById("complication_table").querySelector("tbody").querySelectorAll("tr")
    //     v_complication[td.getAttribute("tr")][td.getAttribute("name")] = td.childNodes[0].value
    // }
    // else if ((td.getAttribute("name") == "inf_oper") || (td.getAttribute("name") == "xosl") || (td.getAttribute("name") == "posl")
    //     || (td.getAttribute("name") == "aosl")) {
    //     v_complication[td.getAttribute("tr")][td.getAttribute("name")] = td.childNodes[0].value

    // }
}

function Complication_delete(td) {
    let v_complication = app.$data.history.sl_oslo
    let complication = []
    
    for (let c = 0; c < v_complication.length; c++) {
        if (c != td.getAttribute("tr")) {
            complication.push(v_complication[c])
        }
    }
    app.$data.history.sl_oslo = complication
    Complication_edit()
    Complication_input()
}