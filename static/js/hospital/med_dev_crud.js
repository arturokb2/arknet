function Med_dev_add() {
    let tbody = document.getElementById("med_dev_table").querySelector("tbody")
    let count = tbody.childNodes
    if (count.length == 0) {
        var n = 0
    }
    else {
        var n = count.length
    }
    let med_l = ['date', 'code', 'number_ser']
    let tr = document.createElement("tr")
    // tr.setAttribute("n", n)
    for (o in med_l) {
        let td = document.createElement("td")
     
        // td.setAttribute("name", med_l[o])
        td.setAttribute("tr", n)
        td.setAttribute("name", med_l[o])
        var ed = document.createElement("input")
        ed.setAttribute("n", n)
        ed.setAttribute("name", med_l[o])
        ed.setAttribute("style", "width:100px")
        // // if (med_l[o] == "date"){

        // // }
        // // else if (med_l[o] == "code"){
        // // }
        // // else if (med_l[o] == "number"){
        // // }
        td.appendChild(ed)
        // // td.setAttribute("name", med_l[o])
        // // td.setAttribute("tr", n)
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
    app.$data.history.med_dev.push(obj)
    Med_dev_edit()
    Med_dev_input()
}
function Med_dev_edit() {
    document.getElementById("med_dev_table").scrollLeft = 0
    let tbody = document.getElementById("med_dev_table").querySelector("tbody")
    tbody.innerHTML = ""
    let v_med_dev = app.$data.history.med_dev
    var n = 0
    if (v_med_dev.length > 0) {
        for (let med_devs in v_med_dev) {
            let med_dev = v_med_dev[med_devs]
            let tr = document.createElement("tr")
            tr.setAttribute("n", n)
            for (m in med_dev) {
                let td = document.createElement("td")
                td.setAttribute('tr',n)
                td.setAttribute('name',m)
                var ed = document.createElement("input")
                ed.setAttribute("n", n)
                ed.setAttribute("name", m)
                ed.value = med_dev[m]
                td.appendChild(ed)
                tr.appendChild(td)
            }
            tbody.appendChild(tr)
            n += 1
        }
        Med_dev_input()
    }
}

function Med_dev_input() {
    let kod =  app.$data.sprav_list.CodeMedDevList
    let str_kod = ''
    for (let k = 0; k < kod.length; k++) {
        str_kod += '<option value="' + kod[k].rzn + '" />'
    }
    var table = document.getElementById("med_dev_table")
    var cells = table.getElementsByTagName("td")
    for (let i = 0; i < cells.length; i++) {
        let input = cells[i].childNodes[0]
        if (cells[i].getAttribute("name") == "date") {
            input.setAttribute("maxlength", 8)
            input.addEventListener("input", function () {
                var n = input.value.replace(/[^0-9]/g, '').split('')
                if (n.length > 2) n.splice(2, 0, '-')
                if (n.length > 4) n.splice(5, 0, '-')
                input.value = n.join('')
            })

        }
        else if  (cells[i].getAttribute("name") == "code") {
            input.setAttribute('list', cells[i].getAttribute("name"))
            let data_list = document.createElement("datalist")
            data_list.setAttribute('id', cells[i].getAttribute("name"))
            data_list.innerHTML = str_kod
            input.appendChild(data_list)
        }
        input.addEventListener("change", function () {
            Med_dev_update(cells[i])
        })
    }
}

function Med_dev_update(td){
    var v_med_dev = app.$data.history.med_dev
    v_med_dev[td.getAttribute("tr")][td.getAttribute("name")] = td.childNodes[0].value

}

function Med_dev_delete(td){
    let v_med_dev = app.$data.history.med_dev
    let med_dev = []

    for (let c = 0; c < v_med_dev.length; c++) {
        if (c != td.getAttribute("tr")) {
            med_dev.push(v_med_dev[c])
        }
    }
    app.$data.history.med_dev = med_dev
    Med_dev_edit()
    Med_dev_input()
}