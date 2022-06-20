
Vue.component('otdel', {
    template: `<div style="display: block;height: 150px;overflow-y: auto;" class="text-center" id="otdel"> 
    <label>Отделения</label>
    <ul>
      <li class="list-group-item" v-for="otde in spravlist.Otde">
        <input type="checkbox" :value="otde['naim']">
        {{otde['naim']}}
      </li>
    </ul>
  </div>`,
    props: ['spravlist']
})

Vue.component('date', {
    template: `<div class="text-center">
        <div><label>за период (дд.мм.гггг)</label></div>
        <label>с</label>
        <input type="date" id="date_r_1">
        <label>по</label>
        <input type="date" id="date_r_2">
        </div>`
})


Vue.component('input_s_po', {
    template: `<div class="text-center">
        <label>с</label>
        <input type="text" id="input_1" style="width:88px">
        <label>по</label>
        <input type="text" id="input_2" style="width:88px">
        </div>`
})
Vue.component('district', {
    template: `<div class="text-center">
                <select class="text-center" style="width: 230px;height: 32px;margin-bottom: 10px;margin-top: 10px;" id="rai">
                <option value="">-----</option>
                <option value="Центральный АО">1.Центральный АО</option>
                <option value="Ленинский АО">2.Ленинский АО</option>
                <option value="Калининский АО">3.Калининский АО</option>
                <option value="Восточный">4.Восточный</option>
                </select>
             </div>`
})

Vue.component('isfin', {
    template: `<div style="display: block;height: 150px;overflow-y: auto;" class="text-center" id="isfin">
    <label>По источникам финансир-я</label>
    <ul>
      <li class="list-group-item" v-for="otde in spravlist.Isfin">
        <input type="checkbox" :value="otde['naim']">
        {{otde['naim']}}
      </li>
    </ul>
  </div>`,
    props: ['spravlist']
})

Vue.component('btn', {
    props: ['btn'],
    template: `<div class="text-center" style="margin-bottom:10px">
    <div>
    <input type="text" value="" id="filename" class="mb-3">
    </div>
    <button v-bind:btn="btn" type="button" id="create_btn_reports" onclick="create_reports(event)" class="btn btn-primary btn-lg" style="padding:0">Создать отчет</button>
    </div>`
})

Vue.component('tit', {
    template: `<div class="text-center" style="margin-top: 10px;">
    {{title}}
  </div>`,
    props: ['title']

})

Vue.component('all_filter', {
    template: `<div class="container">
    <div class="row">
      <div class="col-md-5">
        <ul id="filters_ul">
          <li class="list-group-item"><input type="checkbox" value="datv">Период выбытия</li>
          <li class="list-group-item"><input type="checkbox" value="datp">Период поступления</li>
          <li class="list-group-item"><input type="checkbox" value="otd">Отделение</li>
          <li class="list-group-item"><input type="checkbox" value="prof_k">Профиль койки</li>
          <li class="list-group-item"><input type="checkbox" value="fam">Фимилия (начало фамилии)</li>
          <li class="list-group-item"><input type="checkbox" value="im">Имя (начало имени)</li>
          <li class="list-group-item"><input type="checkbox" value="ot">Отчество (начало отчества)</li>
          <li class="list-group-item"><input type="checkbox" value="pol">Пол</li>
          <li class="list-group-item"><input type="checkbox" value="type_lgots">Тип льготы</li>
          <li class="list-group-item"><input type="checkbox" value="in_t">Льгота</li>
          <li class="list-group-item"><input type="checkbox" value="r_n">Социальный статус</li>
          <li class="list-group-item"><input type="checkbox" value="age_group">Возрастная группа</li>
          <li class="list-group-item"><input type="checkbox" value="goc">Форма госпитализации</li>
          <li class="list-group-item"><input type="checkbox" value="prpg">Вид госпитализации</li>
          <li class="list-group-item"><input type="checkbox" value="vrez">Давность заболевания</li>
          <li class="list-group-item"><input type="checkbox" value="dskz">Ds основной с ...по...</li>
          <li class="list-group-item"><input type="checkbox" value="dsc">Ds сопутствующий</li>
          <li class="list-group-item"><input type="checkbox" value="dspat">Ds патологоанатомический</li>
          <li class="list-group-item"><input type="checkbox" value="dson">Ds онкопатологии</li>
          <li class="list-group-item"><input type="checkbox" value="ksg_osn">КСГ основного Ds</li>
          <li class="list-group-item"><input type="checkbox" value="c_oksm">Гражданство</li>
          <li class="list-group-item"><input type="checkbox" value="terr">Территория проживания</li>
          <li class="list-group-item"><input type="checkbox" value="Регион (обл.,р-н)">Регион (обл.,р-н)</li>
          <li class="list-group-item"><input type="checkbox" value="rai_in">АО г.Тюмень</li>
          <li class="list-group-item"><input type="checkbox" value="cj">Категория проживания</li>
          <li class="list-group-item"><input type="checkbox" value="lpy">Направившее учреждение</li>
          <li class="list-group-item"><input type="checkbox" value="ctkom">Страховая организация</li>
          <li class="list-group-item"><input type="checkbox" value="vds">Источник покрытия затрат</li>
          <li class="list-group-item"><input type="checkbox" value="icx">Исход лечения</li>
          <li class="list-group-item"><input type="checkbox" value="otdel_let">Отд-е летального исхода</li>
          <li class="list-group-item"><input type="checkbox" value="kod_vra">Лечащий врач</li>
          <li class="list-group-item"><input type="checkbox" value="kod_op">Код операции</li>
          <li class="list-group-item"><input type="checkbox" value="pr_osob">Особенность выполнения операции</li>
          <li class="list-group-item"><input type="checkbox" value="t_trv">Тип травмы</li>
          <li class="list-group-item"><input type="checkbox" value="trav_ns">Тип телесных повреждений</li>
          <li class="list-group-item"><input type="checkbox" value="Отметка о замене персон.данных п">Отметка о замене персон.данных п</li>
          <li class="list-group-item"><input type="checkbox" value="disability">Наличие закрытого листа нетрудос</li>
          <li class="list-group-item"><input type="checkbox" value="Дополнительное условие">Дополнительное условие</li>
          <li class="list-group-item"><input type="checkbox" value="wskr">Тип вскрытия(для умерших)</li>
          <li class="list-group-item"><input type="checkbox" value="rasxp">Расхождение с патанатом.Ds</li>
          <li class="list-group-item"><input type="checkbox" value="srber">Срок беременности с ..по..нед</li>
          <li class="list-group-item"><input type="checkbox" value="potd">Внутрибольничный перевод</li>
          <li class="list-group-item"><input type="checkbox" value="kod_y">Перевод в др. ЛПУ</li>
          <li class="list-group-item"><input type="checkbox" value="dskz_prich">Причина травмы</li>
          <li class="list-group-item"><input type="checkbox" value="pr_per">Причина перевода в др.ЛПУ</li>
          <li class="list-group-item"><input type="checkbox" value="time_minuts_po">Длительность пребывания в ПО (мин)</li>
          <li class="list-group-item"><input type="checkbox" value="stay_in_mo">Пребывание в МО (к-дн)</li>
        </ul>
      </div>
      <div class="col-md-7">
        <div id="filters">

        </div>
      </div>
    </div>
  </div>`

})

Vue.component('input_select', {
    template: `<div>
    <input type="text" v-bind:list="ll" v-bind:id="id" style="margin-bottom: 10px;" class="text-center">
    <datalist v-bind:id="ll">
    <option v-for="s in spravlist">{{s[k]}}</option>
    </datalist>
    </div>`,
    props: ['spravlist','k','ll','id']

})

// Vue.component('input_select', {
//     template: `<div>
//     <input type="text" v-bind:list="ll" style="margin-bottom: 10px;" class="text-center">
//     <datalist v-bind:id="ll">
//     <option v-for="s in spravlist">{{s[k]}}<option>
//     </datalist>
//     </div>`,
//     props: ['spravlist','k','ll']

// })

let report_oth = new Vue({

    el: '#report_oth',
    data: {
        lists_references: false,
        annual_reports: false,
        menu_list: false,
        menu_group: false,
        menu_annual: false,
        menu_reports: false,
        report_generation: false,

        //Справочники
        sprav_list: [],
        otdel: false,

        //Отчеты
        g_oth_1: false,
        g_oth_2: false,
        g_oth_3: false,
        g_oth_4: false,
        g_oth_5: false,
        g_oth_6: false,
        g_oth_7: false,
        g_oth_8: false,
        g_oth_9: false,
        g_oth_10: false,
        g_oth_11: false,
        g_oth_12: false,
        g_oth_13: false,
        g_oth_14: false,
        g_oth_15: false,
        g_oth_16: false,
        g_oth_17: false,
        g_oth_18: false,
        g_oth_19: false,
        g_oth_20: false,
        g_oth_21: false,
        g_oth_22: false,
        g_oth_23: false,
        g_oth_24: false,
        g_oth_25: false,

        a_oth_1: false,
        a_oth_2: false,
        a_oth_3: false,
        a_oth_4: false,
        a_oth_5: false,
        a_oth_6: false,
        a_oth_7: false,
        a_oth_8: false,
        a_oth_9: false,
        a_oth_10: false,
        a_oth_11: false,
        a_oth_12: false,
        a_oth_13: false,
        a_oth_14: false,
        a_oth_15: false,
        a_oth_16: false,
        a_oth_17: false,
        a_oth_18: false,
        a_oth_19: false,
        a_oth_20: false,
        a_oth_21: false,
        a_oth_22: false,
        a_oth_23: false,
        a_oth_24: false,
        a_oth_25: false,
        a_oth_26: false,
        a_oth_27: false,
        a_oth_28: false,
        a_oth_29: false,
        a_oth_30: false,
        a_oth_31: false,
        a_oth_32: false,
        a_oth_33: false,


        g_tip_ot_3_2_v: false,
        gla_vra:false,
        isfin_l:false

    },
    mounted: function () {
        this.get_sprav_list()
    },
    methods: {
        get_sprav_list: function () {
            let query = `
       query{
           Otde{
             naim
           },
           Isfin{
            naim
           },
           V020{
            kPrname
          },
          V005{
            polname
          },
          T004{
            name
          },
          RabNer{
            naim
          },
          AgeGroup{
            name
          },
          V014{
            tipName
          },
          Prpg{
            naim
          },
          Vrzb{
            naim
          },
          Oksm{
            naim
           },
           F003{
            naim
          },
          Skom{
            naim
         },
         Isfin{
            naim
         },
         V012{
            idIz
            izName
           },
           Vra{
            kod
          },
          V001{
            kod
         },
         PROsob{
            kod
            naim
        },
        Trv{
            naim
         },
         Trvnas{
            naim
         },
         AbObsh{
                kod
              }
       }`
            return fetch('graph_hospital/', {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query })
            })
                .then(response => response.json())
                .then(data => {
                    this.sprav_list = data.data
                })
                .catch((e) => {
                    // console.log(e)
                })
        },
        init: function () {
            this.lists_references = false
            this.annual_reports = false
            this.menu_list = false
            this.menu_group = false
            this.menu_annual = false
            this.menu_reports = false
            this.report_generation = false
        },
        init_oth: function () {
            this.otdel = false

            this.g_oth_1 = false
            this.g_oth_2 = false
            this.g_oth_3 = false
            this.g_oth_4 = false
            this.g_oth_5 = false
            this.g_oth_6 = false
            this.g_oth_7 = false
            this.g_oth_8 = false
            this.g_oth_9 = false
            this.g_oth_10 = false
            this.g_oth_11 = false
            this.g_oth_12 = false
            this.g_oth_13 = false
            this.g_oth_14 = false
            this.g_oth_15 = false
            this.g_oth_16 = false
            this.g_oth_17 = false
            this.g_oth_18 = false
            this.g_oth_19 = false
            this.g_oth_20 = false
            this.g_oth_21 = false
            this.g_oth_22 = false
            this.g_oth_23 = false
            this.g_oth_24 = false
            this.g_oth_25 = false

            this.a_oth_1 = false
            this.a_oth_2 = false
            this.a_oth_3 = false
            this.a_oth_4 = false
            this.a_oth_5 = false
            this.a_oth_6 = false
            this.a_oth_7 = false
            this.a_oth_8 = false
            this.a_oth_9 = false
            this.a_oth_10 = false
            this.a_oth_11 = false
            this.a_oth_12 = false
            this.a_oth_13 = false
            this.a_oth_14 = false
            this.a_oth_15 = false
            this.a_oth_16 = false
            this.a_oth_17 = false
            this.a_oth_18 = false
            this.a_oth_19 = false
            this.a_oth_20 = false
            this.a_oth_21 = false
            this.a_oth_22 = false
            this.a_oth_23 = false
            this.a_oth_24 = false
            this.a_oth_25 = false
            this.a_oth_26 = false
            this.a_oth_27 = false
            this.a_oth_28 = false
            this.a_oth_29 = false
            this.a_oth_30 = false
            this.a_oth_31 = false
            this.a_oth_32 = false
            this.a_oth_33 = false

        },
        references: function () {
            this.init()
            this.init_oth()

            this.lists_references = !this.lists_references
            this.annual_reports = false
            this.menu_reports = false
            this.menu_group = false
            this.menu_annual = false


        },
        reports: function () {
            this.init()
            this.init_oth()

            this.annual_reports = !this.annual_reports
            this.lists_references = false
            this.menu_group = false
            this.menu_annual = false
            this.report_generation = false
            this.menu_reports = false

        },
        group: function () {
            this.init_oth()
            this.menu_group = !this.menu_group
            this.menu_annual = false
        },
        annual: function () {
            this.init_oth()
            this.menu_annual = !this.menu_annual
            this.menu_group = false
        },
        generation: function () {
            this.report_generation = !this.report_generation
            this.menu_reports = false
        },
        reports_menu: function () {
            this.menu_reports = !this.menu_reports
            this.report_generation = false
        },

        group_oth_1: function () {
            this.init_oth()
            this.g_oth_1 = true
        },
        group_oth_2: function () {
            this.init_oth()
            this.g_oth_2 = true
            setTimeout(() => {
                all_filters()
            }, 300);
        },
        group_oth_3: function () {
            this.init_oth()
            this.g_oth_3 = true
        },
        group_oth_4: function () {
            this.init_oth()
            this.g_oth_4 = true
            setTimeout(() => {
                all_filters()
            }, 300);
        },
        group_oth_5: function () {
            this.init_oth()
            this.g_oth_5 = true
        },
        group_oth_6: function () {
            this.init_oth()
            this.g_oth_6 = true
        },
        group_oth_7: function () {
            this.init_oth()
            this.g_oth_7 = true
        },
        group_oth_8: function () {
            this.init_oth()
            this.g_oth_8 = true
        },
        group_oth_9: function () {
            this.init_oth()
            this.g_oth_9 = true
        },
        group_oth_10: function () {
            this.init_oth()
            this.g_oth_10 = true
        },
        group_oth_11: function () {
            this.init_oth()
            this.g_oth_11 = true
        },
        group_oth_12: function () {
            this.init_oth()
            this.g_oth_12 = true
        },
        group_oth_13: function () {
            this.init_oth()
            this.g_oth_13 = true
        },
        group_oth_14: function () {
            this.init_oth()
            this.g_oth_14 = true
        },
        group_oth_15: function () {
            this.init_oth()
            this.g_oth_15 = true
        },
        group_oth_16: function () {
            this.init_oth()
            this.g_oth_16 = true
        },
        group_oth_17: function () {
            this.init_oth()
            this.g_oth_17 = true
        },
        group_oth_1: function () {
            this.init_oth()
            this.g_oth_1 = true
        },
        group_oth_18: function () {
            this.init_oth()
            this.g_oth_18 = true
        },
        group_oth_19: function () {
            this.init_oth()
            this.g_oth_19 = true
        },
        group_oth_20: function () {
            this.init_oth()
            this.g_oth_20 = true
        },
        group_oth_21: function () {
            this.init_oth()
            this.g_oth_21 = true
        },
        group_oth_22: function () {
            this.init_oth()
            this.g_oth_22 = true
        },
        group_oth_23: function () {
            this.init_oth()
            this.g_oth_23 = true
        },
        group_oth_24: function () {
            this.init_oth()
            this.g_oth_24 = true
        },
        group_oth_25: function () {
            this.init_oth()
            this.g_oth_25 = true
        },


        annual_oth_1: function () {
            this.init_oth()
            this.a_oth_1 = true
        },
        annual_oth_2: function () {
            this.init_oth()
            this.a_oth_2 = true
        },
        annual_oth_3: function () {
            this.init_oth()
            this.a_oth_3 = true
        },
        annual_oth_4: function () {
            this.init_oth()
            this.a_oth_4 = true
        },
        annual_oth_5: function () {
            this.init_oth()
            this.a_oth_5 = true
        },
        annual_oth_6: function () {
            this.init_oth()
            this.a_oth_6 = true
        },
        annual_oth_7: function () {
            this.init_oth()
            this.a_oth_7 = true
        },
        annual_oth_8: function () {
            this.init_oth()
            this.a_oth_8 = true
        },
        annual_oth_9: function () {
            this.init_oth()
            this.a_oth_9 = true
        },
        annual_oth_10: function () {
            this.init_oth()
            this.a_oth_10 = true
        },
        annual_oth_11: function () {
            this.init_oth()
            this.a_oth_11 = true
        },
        annual_oth_12: function () {
            this.init_oth()
            this.a_oth_12 = true
        },
        annual_oth_13: function () {
            this.init_oth()
            this.a_oth_13 = true
        },
        annual_oth_14: function () {
            this.init_oth()
            this.a_oth_14 = true
        },
        annual_oth_15: function () {
            this.init_oth()
            this.a_oth_15 = true
        },
        annual_oth_16: function () {
            this.init_oth()
            this.a_oth_16 = true
        },
        annual_oth_17: function () {
            this.init_oth()
            this.a_oth_17 = true
        },
        annual_oth_18: function () {
            this.init_oth()
            this.a_oth_18 = true
        },
        annual_oth_19: function () {
            this.init_oth()
            this.a_oth_19 = true
        },
        annual_oth_20: function () {
            this.init_oth()
            this.a_oth_20 = true
        },
        annual_oth_21: function () {
            this.init_oth()
            this.a_oth_21 = true
        },
        annual_oth_22: function () {
            this.init_oth()
            this.a_oth_22 = true
        },
        annual_oth_23: function () {
            this.init_oth()
            this.a_oth_23 = true
        },
        annual_oth_24: function () {
            this.init_oth()
            this.a_oth_24 = true
        },
        annual_oth_25: function () {
            this.init_oth()
            this.a_oth_25 = true
        },
        annual_oth_26: function () {
            this.init_oth()
            this.a_oth_26 = true
        },
        annual_oth_27: function () {
            this.init_oth()
            this.a_oth_27 = true
        },
        annual_oth_28: function () {
            this.init_oth()
            this.a_oth_28 = true
        },
        annual_oth_29: function () {
            this.init_oth()
            this.a_oth_29 = true
        },
        annual_oth_30: function () {
            this.init_oth()
            this.a_oth_30 = true
        },
        annual_oth_31: function () {
            this.init_oth()
            this.a_oth_31 = true
        },
        annual_oth_32: function () {
            this.init_oth()
            this.a_oth_32 = true
        },
        annual_oth_33: function () {
            this.init_oth()
            this.a_oth_33 = true
        }

    }

})


function init() {
    report_oth.init()
    report_oth.init_oth()
}

function onchange_g_select_tip_ot_1(event) {
    if (event.target.value == 'по отделению') {
        report_oth.$data.otdel = true
    }
    else {
        report_oth.$data.otdel = false
    }

    if (event.target.value == 'Для зам.гл.врача'){
        report_oth.$data.gla_vra = true
    }
    else {
        report_oth.$data.gla_vra = false
    }
}

function onchange_g_select_tip_ot_3_1(event) {
    if (event.target.value == 'по подразделениям ЛУ') {
        report_oth.$data.g_tip_ot_3_2_v = true
    }
    else {
        report_oth.$data.g_tip_ot_3_2_v = false
    }
}

function onchange_g_isfin(event) {
    if (event.target.value == 'по источникам финансир-я') {
        report_oth.$data.isfin_l = true
    }
    else {
        report_oth.$data.isfin_l = false
    }
}




function all_filters() {
    let list_li = document.getElementById("filters_ul").querySelectorAll('li')
    let filters = document.getElementById("filters")
    let type_lgots = ['Территориальная', 'Федеральная']
    for (let li of list_li) {
        li.firstChild.addEventListener("click", function () {
            let div_title = document.createElement("div")
            div_title.setAttribute("id", this.value + "_title")
            let label = document.createElement("label")
            label.innerHTML = this.nextSibling.nodeValue
            div_title.appendChild(label)

            let div_block = document.createElement("div")
            div_block.setAttribute("id", this.value + "_block")

            if (this.value == 'datv' || this.value == 'datp' || this.value == 'dskz' || this.value == 'dsc'
                || this.value == 'dspat' || this.value == 'dson' || this.value == 'srber' || this.value == 'dskz_prich') {
                let dat_1 = document.createElement("input")
                dat_1.setAttribute("style", "width:88px")
                let dat_2 = document.createElement("input")
                dat_2.setAttribute("style", "width:88px")
                let lab_1 = document.createElement("label")
                lab_1.innerHTML = 'C'
                let lab_2 = document.createElement("label")
                lab_2.innerHTML = 'по'
                div_block.appendChild(lab_1)
                div_block.appendChild(dat_1)
                div_block.appendChild(lab_2)
                div_block.appendChild(dat_2)
            }
            else if (this.value == 'otd' || this.value == 'prof_k' || this.value == 'pol' || this.value == 'type_lgots'
                || this.value == 'in_t' || this.value == 'r_n' || this.value == 'age_group' || this.value == 'goc'
                || this.value == 'prpg' || this.value == 'vrez' || this.value == 'c_oksm' || this.value == 'terr'
                || this.value == 'rai_in' || this.value == 'cj' || this.value == 'lpy' || this.value == 'ctkom'
                || this.value == 'vds' || this.value == 'icx' || this.value == 'otdel_let' || this.value == 'kod_vra'
                || this.value == 'kod_op' || this.value == 'pr_osob' || this.value == 't_trv' || this.value == 'trav_ns'
                || this.value == 'wskr' || this.value == 'rasxp' || this.value == 'potd' || this.value == 'kod_y'
                || this.value == 'pr_per') {
                var inp = document.createElement("input")
                var dat_l = document.createElement("datalist")
                if (this.value == 'otd') {
                    inp.setAttribute("list", "otdel_l")
                    dat_l.setAttribute("id", "otdel_l")
                    var list = report_oth.$data.sprav_list.Otde
                }
                else if (this.value == 'prof_k') {
                    inp.setAttribute("list", "prof_k_l")
                    dat_l.setAttribute("id", "prof_k_l")
                    var list = report_oth.$data.sprav_list.V020
                }
                else if (this.value == 'pol') {
                    inp.setAttribute("list", "pol_l")
                    dat_l.setAttribute("id", "pol_l")
                    var list = report_oth.$data.sprav_list.V005
                }
                else if (this.value == 'type_lgots') {
                    inp.setAttribute("list", "type_lgots_l")
                    dat_l.setAttribute("id", "type_lgots_l")
                    var list = type_lgots
                }
                else if (this.value == 'in_t') {
                    inp.setAttribute("list", "in_t_l")
                    dat_l.setAttribute("id", "in_t_l")
                    var list = report_oth.$data.sprav_list.T004
                }
                else if (this.value == 'r_n') {
                    inp.setAttribute("list", "r_n_l")
                    dat_l.setAttribute("id", "r_n_l")
                    var list = report_oth.$data.sprav_list.RabNer
                }
                else if (this.value == 'age_group') {
                    inp.setAttribute("list", "age_group_l")
                    dat_l.setAttribute("id", "age_group_l")
                    var list = report_oth.$data.sprav_list.AgeGroup
                }
                else if (this.value == 'goc') {
                    inp.setAttribute("list", "goc_l")
                    dat_l.setAttribute("id", "goc_l")
                    var list = report_oth.$data.sprav_list.V014
                }
                else if (this.value == 'prpg') {
                    inp.setAttribute("list", "prpg_l")
                    dat_l.setAttribute("id", "prpg_l")
                    var list = report_oth.$data.sprav_list.Prpg
                }
                else if (this.value == 'vrez') {
                    inp.setAttribute("list", "vrez_l")
                    dat_l.setAttribute("id", "vrez_l")
                    var list = report_oth.$data.sprav_list.Vrzb
                }
                else if (this.value == 'c_oksm') {
                    inp.setAttribute("list", "c_oksm_l")
                    dat_l.setAttribute("id", "c_oksm_l")
                    var list = report_oth.$data.sprav_list.Oksm
                }
                else if (this.value == 'terr') {
                    inp.setAttribute("list", "terr_l")
                    dat_l.setAttribute("id", "terr_l")
                    var list = ['г.Тюменю', '1 Юг Тюм.обл.кроме Тюм.р-н', '2 Тюменский р-н', '3 Ханты-Мансйский АО',
                        '4 Ямало-Немецкий АО', '5 Др.регионы Россий', 'Др. государства']
                }
                else if (this.value == 'rai_in') {
                    inp.setAttribute("list", "rai_in_l")
                    dat_l.setAttribute("id", "rai_in_l")
                    var list = ['Центральный АО', 'Ленинский АО', 'Калининский АО', 'Восточный АО']
                }
                else if (this.value == 'cj') {
                    inp.setAttribute("list", "cj_l")
                    dat_l.setAttribute("id", "cj_l")
                    var list = ['Городской', 'Сельский']
                }
                else if (this.value == 'lpy') {
                    inp.setAttribute("list", "lpy_l")
                    dat_l.setAttribute("id", "lpy_l")
                    var list = report_oth.$data.sprav_list.F003
                }
                else if (this.value == 'ctkom') {
                    inp.setAttribute("list", "ctkom_l")
                    dat_l.setAttribute("id", "ctkom_l")
                    var list = report_oth.$data.sprav_list.Skom
                }
                else if (this.value == 'vds') {
                    inp.setAttribute("list", "vds_l")
                    dat_l.setAttribute("id", "vds_l")
                    var list = report_oth.$data.sprav_list.Isfin
                }
                else if (this.value == 'icx') {
                    inp.setAttribute("list", "icx_l")
                    dat_l.setAttribute("id", "icx_l")
                    var list = report_oth.$data.sprav_list.V012
                }
                else if (this.value == 'otdel_let') {
                    inp.setAttribute("list", "otdel_let_l")
                    dat_l.setAttribute("id", "otdel_let_l")
                    var list = ['Отделение по поступлению', 'Приемное', 'АРО1(Анестезия и рем)', 'АРО2(Интен.,невролог.)',
                        'АРО2(Нейрореанимация)', 'АРО3']
                }
                else if (this.value == 'kod_vra') {
                    inp.setAttribute("list", "kod_vra_l")
                    dat_l.setAttribute("id", "kod_vra_l")
                    var list = report_oth.$data.sprav_list.Vra
                }
                else if (this.value == 'kod_op') {
                    inp.setAttribute("list", "kod_op_l")
                    dat_l.setAttribute("id", "kod_op_l")
                    var list = report_oth.$data.sprav_list.V001
                }
                else if (this.value == 'pr_osob') {
                    inp.setAttribute("list", "pr_osob_l")
                    dat_l.setAttribute("id", "pr_osob_l")
                    var list = report_oth.$data.sprav_list.PROsob
                }
                else if (this.value == 't_trv') {
                    inp.setAttribute("list", "t_trv_l")
                    dat_l.setAttribute("id", "t_trv_l")
                    var list = report_oth.$data.sprav_list.Trv
                }
                else if (this.value == 'trav_ns') {
                    inp.setAttribute("list", "trav_ns_l")
                    dat_l.setAttribute("id", "trav_ns_l")
                    var list = report_oth.$data.sprav_list.Trvnas
                }
                else if (this.value == 'wskr') {
                    inp.setAttribute("list", "wskr_l")
                    dat_l.setAttribute("id", "wskr_l")
                    var list = ['без вскрытия', 'патологоанатом.', 'судебное']
                }
                else if (this.value == 'rasxp') {
                    inp.setAttribute("list", "rasxp_l")
                    dat_l.setAttribute("id", "rasxp_l")
                    var list = ['да', 'нет']
                }

                else if (this.value == 'potd') {
                    inp.setAttribute("list", "potd_l")
                    dat_l.setAttribute("id", "potd_l")
                    var list = report_oth.$data.sprav_list.Otde
                }
                else if (this.value == 'kod_y') {
                    inp.setAttribute("list", "kod_y_l")
                    dat_l.setAttribute("id", "kod_y_l")
                    var list = report_oth.$data.sprav_list.F003
                }
                else if (this.value == 'pr_per') {
                    inp.setAttribute("list", "pr_per_l")
                    dat_l.setAttribute("id", "pr_per_l")
                    var list = ['для оказания специализированной мед.помощи', 'для прохождения реабилитации', 'для следующего этапа лечения']
                }

                for (o of list) {
                    var op = document.createElement("option")
                    if (this.value == 'otd') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'prof_k') {
                        op.value = o.kPrname
                        op.innerText = o.kPrname
                    }
                    else if (this.value == 'pol') {
                        op.value = o.polname
                        op.innerText = o.polname
                    }
                    else if (this.value == 'type_lgots') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.value == 'in_t') {
                        op.value = o.name
                        op.innerText = o.name
                    }
                    else if (this.value == 'r_n') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'age_group') {
                        op.value = o.name
                        op.innerText = o.name
                    }
                    else if (this.value == 'goc') {
                        op.value = o.tipName
                        op.innerText = o.tipName
                    }
                    else if (this.value == 'prpg') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'vrez') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'c_oksm') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'terr') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.value == 'rai_in') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.value == 'cj') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.value == 'lpy') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'ctkom') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'vds') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'icx') {
                        op.value = o.idIz + ' ' + o.izName
                        op.innerText = o.idIz + ' ' + o.izName
                    }
                    else if (this.value == 'otdel_let') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.value == 'kod_vra') {
                        op.value = o.kod
                        op.innerText = o.kod
                    }
                    else if (this.value == 'kod_op') {
                        op.value = o.kod
                        op.innerText = o.kod
                    }
                    else if (this.value == 'pr_osob') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 't_trv') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'trav_ns') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'wskr') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.value == 'rasxp') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.value == 'potd') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'kod_y') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.value == 'pr_per') {
                        op.value = o
                        op.innerText = o
                    }

                    dat_l.appendChild(op)
                }
                if (this.value == 'potd' || this.value == 'kod_y') {
                    var op = document.createElement("option")
                    op.value = 'все переводы'
                    op.innerText = 'все переводы'
                }
                dat_l.appendChild(op)
                div_block.appendChild(inp)
                div_block.appendChild(dat_l)
            }

            else if (this.value == 'fam' || this.value == 'im' || this.value == 'ot' || this.value == 'ksg_osn'
                || this.value == 'time_minuts_po' || this.value == 'stay_in_mo') {
                var inp = document.createElement("input")
                div_block.appendChild(inp)
            }
            else if (this.value == 'disability') {
                var lab = document.createElement("label")
                lab.innerHTML = "Поиск по нетрудоспособности"
                div_block.appendChild(lab)
            }


            if (this.checked) {
                filters.appendChild(div_title)
                filters.appendChild(div_block)

            }
            else {
                filters.removeChild(document.getElementById(this.value + "_title"))
                filters.removeChild(document.getElementById(this.value + "_block"))
            }
        })
    }
}


function create_reports(event) {
    let type_report = event.target.getAttribute("btn")

    if (type_report == 'g_oth_1'){g_oth_1_f(type_report)}
    else if (type_report == 'g_oth_2'){g_oth_2_f(type_report)}
    else if (type_report == 'g_oth_3'){g_oth_3_f(type_report)}
    else if (type_report == 'g_oth_4'){g_oth_4_f(type_report)}
    else if (type_report == 'g_oth_5'){g_oth_5_f(type_report)}
    else if (type_report == 'g_oth_6'){g_oth_6_f(type_report)}
    else if (type_report == 'g_oth_7'){g_oth_7_f(type_report)}
    else if (type_report == 'g_oth_8'){g_oth_8_f(type_report)}
    else if (type_report == 'g_oth_9'){g_oth_9_f(type_report)}
    else if (type_report == 'g_oth_10'){g_oth_10_f(type_report)}
    else if (type_report == 'g_oth_11'){g_oth_11_f(type_report)}
    else if (type_report == 'g_oth_12'){g_oth_12_f(type_report)}
    else if (type_report == 'g_oth_13'){g_oth_13_f(type_report)}
    else if (type_report == 'g_oth_14'){g_oth_14_f(type_report)}
    else if (type_report == 'g_oth_15'){g_oth_15_f(type_report)}
    else if (type_report == 'g_oth_16'){g_oth_16_f(type_report)}
    else if (type_report == 'g_oth_17'){g_oth_17_f(type_report)}
    else if (type_report == 'g_oth_18'){g_oth_18_f(type_report)}
    else if (type_report == 'g_oth_19'){g_oth_19_f(type_report)}
    else if (type_report == 'g_oth_20'){g_oth_20_f(type_report)}
    else if (type_report == 'g_oth_21'){g_oth_21_f(type_report)}
    else if (type_report == 'g_oth_22'){g_oth_22_f(type_report)}
    else if (type_report == 'g_oth_23'){g_oth_23_f(type_report)}
    else if (type_report == 'g_oth_24'){g_oth_24_f(type_report)}
    else if (type_report == 'g_oth_25'){g_oth_25_f(type_report)}

}

function g_oth_1_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let select = document.getElementById("tip_ot_1")
    let otdel = document.getElementById("otdel")
    let otdel_checked = get_checked_input(otdel)
    let filename = document.getElementById("filename")
    var formData = new FormData()
    formData.append('report_type',type_report)
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('select',select!= null ? select.value : '')
    formData.append('otdel',otdel_checked)
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

    if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_2_f(type_report) {
}

function g_oth_3_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let select_1 = document.getElementById("tip_ot_3_1")
    let select_2 = document.getElementById("tip_ot_3_2")
    let otdel = document.getElementById("otdel")
    let otdel_checked = get_checked_input(otdel)
    let filename = document.getElementById("filename")
    var formData = new FormData()
    formData.append('report_type',type_report)
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('select_1',select_1 != null ? select_1.value : '')
    formData.append('select_2',select_2 != null ? select_2.value : '')
    formData.append('otdel',otdel_checked)
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

    if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_4_f(type_report) {
}

function g_oth_5_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let day_n = document.getElementById("n")
    let filename = document.getElementById("filename")
    var formData = new FormData()
    formData.append('report_type',type_report)
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('day_n',day_n.value)
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

    if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_6_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let oper = document.getElementById("v001")
    let filename = document.getElementById("filename")
    var formData = new FormData()
    formData.append('report_type',type_report)
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('oper',oper.value)
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

    if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_7_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let filename = document.getElementById("filename")
    var formData = new FormData()
    formData.append('report_type',type_report)
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

    if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_8_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let input_ds_1 = document.getElementById("input_1")
    let input_ds_2 = document.getElementById("input_2")
    let filename = document.getElementById("filename")
    var formData = new FormData()
    formData.append('report_type',type_report)
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('input_ds_1',input_ds_1.value)
    formData.append('input_ds_2',input_ds_2.value)
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

    if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_9_f(type_report) {
    let dat = document.getElementById("date")
    let select_1 = document.getElementById("tip_ot_9_1")
    let select_2 = document.getElementById("tip_ot_9_2")
    let otdel = document.getElementById("otdel")
    let otdel_checked = get_checked_input(otdel)
    let filename = document.getElementById("filename")
    var formData = new FormData()
    formData.append('report_type',type_report)
    formData.append('date',dat != null ? dat.value : '')
    formData.append('select_1',select_1!= null ? select_1.value : '')
    formData.append('select_2',select_2!= null ? select_2.value : '')
    formData.append('otdel',otdel_checked)
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

    if (dat.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_10_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let rai = document.getElementById("rai")
    let filename = document.getElementById("filename")
    var formData = new FormData()
    formData.append('report_type',type_report)
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('rai',rai!= null ? rai.value : '')
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

    if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }

}

function g_oth_11_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let select_1 = document.getElementById("tip_ot_11_1")
    let isfin = document.getElementById("isfin")
    let isfin_checked = get_checked_input(isfin)
    let hist = document.getElementById("search_input_hist")
    let select_2 = document.getElementById("tip_ot_11_2")
    let filename = document.getElementById("filename")
    var formData = new FormData()
    formData.append('report_type',type_report)
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('select_1',select_1!= null ? select_1.value : '')
    formData.append('isfin',isfin_checked)
    formData.append('hist',hist.value)
    formData.append('select_2',select_2!= null ? select_2.value : '')
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

    if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_12_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let select_1 = document.getElementById("tip_ot_12_1")
    let otdel = document.getElementById("otdel")
    let otdel_checked = get_checked_input(otdel)
    let filename = document.getElementById("filename")

    var formData = new FormData()
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('select_1',select_1!= null ? select_1.value : '')
    formData.append('otdel',otdel_checked)
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

    if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_13_f(type_report) {
}

function g_oth_14_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let filename = document.getElementById("filename")
    var formData = new FormData()
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

     if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_15_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let abobsh = document.getElementById("abobsh")
    let vra = document.getElementById("vra")
    let otdel = document.getElementById("otdel")
    let fam_pat = document.getElementById("fam_pat")
    let agegroup = document.getElementById("agegroup")
    let v014 = document.getElementById("v014")
    let prpg = document.getElementById("prpg")
    let v005 = document.getElementById("v005")
    let input_1 = document.getElementById("input_1")
    let input_2 = document.getElementById("input_2")
    let v012 = document.getElementById("v012")
    let filename = document.getElementById("filename")

    var formData = new FormData()
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('abobsh',abobsh.value)
    formData.append('vra',vra.value)
    formData.append('otdel',otdel.value)
    formData.append('fam_pat',fam_pat.value)
    formData.append('agegroup',agegroup.value)
    formData.append('v014',v014.value)
    formData.append('prpg',prpg.value)
    formData.append('v005',v005.value)
    formData.append('input_1',input_1.value)
    formData.append('input_2',input_2.value)
    formData.append('v012',v012.value)
    formData.append('filename',filename.value)

    if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }


}

function g_oth_16_f(type_report) {
    let day_n = document.getElementById("day_n")
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let filename = document.getElementById("filename")

    var formData = new FormData()
    formData.append('day_n',day_n.value)
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

     if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_17_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let filename = document.getElementById("filename")

    var formData = new FormData()
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

     if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_18_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let filename = document.getElementById("filename")

    var formData = new FormData()
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

     if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_19_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let filename = document.getElementById("filename")

    var formData = new FormData()
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

     if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_20_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let filename = document.getElementById("filename")

    var formData = new FormData()
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

     if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_21_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let filename = document.getElementById("filename")

    var formData = new FormData()
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

     if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_22_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let otdel = document.getElementById("otdel")
    let vid_vtmp = document.getElementById("vid_vtmp")
    let met_vtmp = document.getElementById("met_vtmp")
    let filename = document.getElementById("filename")

    var formData = new FormData()
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('otdel',otdel.value)
    formData.append('vid_vtmp',vid_vtmp.value)
    formData.append('met_vtmp',met_vtmp.value)
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

     if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_23_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let filename = document.getElementById("filename")

    var formData = new FormData()
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

     if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function g_oth_24_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let input_1 = document.getElementById("input_1")
    let input_2 = document.getElementById("input_2")
    let terr = document.getElementById("terr")
    let f003 = document.getElementById("f003")
    let select_1 = document.getElementById("tip_ot_24_1")
    let filename = document.getElementById("filename")


    var formData = new FormData()
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('input_1',input_1.value)
    formData.append('input_2',input_2.value)
    formData.append('terr',terr.value)
    formData.append('f003',f003.value)
    formData.append('select_1',select_1.value)
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb')

    if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }

}

function g_oth_25_f(type_report) {
    let dat_1 = document.getElementById("date_r_1")
    let dat_2 = document.getElementById("date_r_2")
    let filename = document.getElementById("filename")

    var formData = new FormData()
    formData.append('date_1',dat_1 != null ? dat_1.value : '')
    formData.append('date_2',dat_2 != null ? dat_2.value : '')
    formData.append('filename',filename.value)
    formData.append('task_type','kcc_cb') 

     if (dat_1.value != '' && dat_2.value != ''){
        sendRequest_f(formData)
    }
}

function sendRequest_f(formData) {
    var r = sendRequest('reports/', 'post', formData)
    .then(response => {
        console.log(response.data.rez)
    })
    .catch(error => {
        })
}

function get_checked_input(ul) {
    if (ul != null && ul != undefined){
        let list_input = ul.querySelectorAll("input")
        let checked_input = []
        for (input of list_input){
            if (input.checked){
                checked_input.push(input.value)
            }
        }
        return checked_input
    }
    return ''

}