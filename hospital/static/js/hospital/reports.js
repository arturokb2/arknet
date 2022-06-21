


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

// Vue.component('Trv', {
//     template: `<div style="display: block;height: 150px;overflow-y: auto;" class="text-center" id="otdel"> 
//     <label>Тип травмы</label>
//     {{sprav_list.Trv}}
//     <ul>
//       <li class="list-group-item" v-for="t in sprav_list.Trv">
//         <input type="checkbox" :value="t['naim']">
//         {{t['naim']}}
//       </li>
//     </ul>
//   </div>`
// })

Vue.component('date', {
    template: `<div class="text-center">
        <div><label>за период (дд.мм.гггг)</label></div>
        <label>с</label>
        <input type="date" id="date1">
        <label>по</label>
        <input type="date" id="date2">
        </div>`
})

Vue.component('date_', {
    template: `<div class="text-center">
        <div><label>за период (дд.мм.гггг)</label></div>
        <label>с</label>
        <input type="date" :name="name1">
        <label>по</label>
        <input type="date" :name="name2">
        </div>`,
    props: ['name1', 'name2']
})


Vue.component('dskz', {
    template: `
    <div class="text-center">
        <tit title="Диагноз (МКБ10)"></tit>
        <label>с</label>
        <input type="text" :name="name1" style="width: 88px;">
        <label>по</label>
        <input type="text" :name="name2" style="width: 88px;">
        </div>`,
    props: ['name1', 'name2']
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
    template: `<div id="menu-list">
        <ul id="filters_ul">
          <li class="list-group-item"><input type="checkbox" id="datv_filt">Период выбытия</li>
          <li class="list-group-item"><input type="checkbox" id="datp_filt">Период поступления</li>
          <li class="list-group-item"><input type="checkbox" id="otd_filt">Отделение</li>
          <li class="list-group-item"><input type="checkbox" id="prof_filt">Профиль койки</li>
          <li class="list-group-item"><input type="checkbox" id="fam_filt">Фимилия (начало фамилии)</li>
          <li class="list-group-item"><input type="checkbox" id="im_filt">Имя (начало имени)</li>
          <li class="list-group-item"><input type="checkbox" id="ot_filt">Отчество (начало отчества)</li>
          <li class="list-group-item"><input type="checkbox" id="pol_filt">Пол</li>
          <li class="list-group-item"><input type="checkbox" id="type_lgots_filt">Тип льготы</li>
          <li class="list-group-item"><input type="checkbox" id="in_t_filt">Льгота</li>
          <li class="list-group-item"><input type="checkbox" id="r_n_filt">Социальный статус</li>
          <li class="list-group-item"><input type="checkbox" id="age_group_filt">Возрастная группа</li>
          <li class="list-group-item"><input type="checkbox" id="goc_filt">Форма госпитализации</li>
          <li class="list-group-item"><input type="checkbox" id="prpg_filt">Вид госпитализации</li>
          <li class="list-group-item"><input type="checkbox" id="vrez_filt">Давность заболевания</li>
          <li class="list-group-item"><input type="checkbox" id="dskz_filt">Ds основной с ...по...</li>
          <li class="list-group-item"><input type="checkbox" id="dsc_filt">Ds сопутствующий</li>
          <li class="list-group-item"><input type="checkbox" id="dspat_filt">Ds патологоанатомический</li>
          <li class="list-group-item"><input type="checkbox" id="dson_filt">Ds онкопатологии</li>
          <li class="list-group-item"><input type="checkbox" id="ksg_osn_filt">КСГ основного Ds</li>
          <li class="list-group-item"><input type="checkbox" id="c_oksm_filt">Гражданство</li>
          <li class="list-group-item"><input type="checkbox" id="terr_filt">Территория проживания</li>
          <li class="list-group-item"><input type="checkbox" id="reg_obl_rai_filt">Регион (обл.,р-н)</li>
          <li class="list-group-item"><input type="checkbox" id="rai_in_filt">АО г.Тюмень</li>
          <li class="list-group-item"><input type="checkbox" id="cj_filt">Категория проживания</li>
          <li class="list-group-item"><input type="checkbox" id="lpy_filt">Направившее учреждение</li>
          <li class="list-group-item"><input type="checkbox" id="ctkom_filt">Страховая организация</li>
          <li class="list-group-item"><input type="checkbox" id="vds_filt">Источник покрытия затрат</li>
          <li class="list-group-item"><input type="checkbox" id="icx_filt">Исход лечения</li>
          <li class="list-group-item"><input type="checkbox" id="otdel_let_filt">Отд-е летального исхода</li>
          <li class="list-group-item"><input type="checkbox" id="kod_vra_filt">Лечащий врач</li>
          <li class="list-group-item"><input type="checkbox" id="kod_op_filt">Код операции</li>
          <li class="list-group-item"><input type="checkbox" id="pr_osob_filt">Особенность выполнения операции</li>
          <li class="list-group-item"><input type="checkbox" id="t_trv_filt">Тип травмы</li>
          <li class="list-group-item"><input type="checkbox" id="trav_ns_filt">Тип телесных повреждений</li>
          <li class="list-group-item"><input type="checkbox" id="disability_filt">Наличие закрытого листа нетрудос</li>
          <li class="list-group-item"><input type="checkbox" id="wskr_filt">Тип вскрытия(для умерших)</li>
          <li class="list-group-item"><input type="checkbox" id="rasxp_filt">Расхождение с патанатом.Ds</li>
          <li class="list-group-item"><input type="checkbox" id="srber_filt">Срок беременности с ..по..нед</li>
          <li class="list-group-item"><input type="checkbox" id="potd_filt">Внутрибольничный перевод</li>
          <li class="list-group-item"><input type="checkbox" id="kod_y_filt">Перевод в др. ЛПУ</li>
          <li class="list-group-item"><input type="checkbox" id="dskz_prich_filt">Причина травмы</li>
          <li class="list-group-item"><input type="checkbox" id="pr_per_filt">Причина перевода в др.ЛПУ</li>
          <li class="list-group-item"><input type="checkbox" id="time_minuts_po_filt">Длительность пребывания в ПО (мин)</li>
          <li class="list-group-item"><input type="checkbox" id="stay_in_mo_filt">Пребывание в МО (к-дн)</li>
          <li class="list-group-item"><input type="checkbox" id="man_list">Список манипуляции</li>
          <li class="list-group-item"><input type="checkbox" id="metod_hmp">Вид ВТМП</li>
          <li class="list-group-item"><input type="checkbox" id="vid_hmp">Методы ВТМП</li>
        </ul>
  </div>`
})

Vue.component('all_input_models', {
    template: `<div id="menu-group">
    <ul id="list_data">
      <li class="list-group-item"><b>Персональные данные</b></li>
      <li class="list-group-item"><input type="checkbox" id="nib">История</li>
      <li class="list-group-item"><input type="checkbox" id="fam">Фимилия</li>
      <li class="list-group-item"><input type="checkbox" id="im">Имя</li>
      <li class="list-group-item"><input type="checkbox" id="ot">Отчество</li>
      <li class="list-group-item"><input type="checkbox" id="pol">Пол</li>
      <li class="list-group-item"><input type="checkbox" id="datp">Дата поступления</li>
      <li class="list-group-item"><input type="checkbox" id="tm_otd">Время</li>
      <li class="list-group-item"><input type="checkbox" id="datv">Дата выписки</li>
      <li class="list-group-item"><input type="checkbox" id="datr">Дата рождения</li>
      <li class="list-group-item"><input type="checkbox" id="otd">Отделение</li>
      <li class="list-group-item"><input type="checkbox" id="m_roj_in">Адрес рождения</li>
      <li class="list-group-item"><input type="checkbox" id="adr_in">Адрес регистрации</li>
      <li class="list-group-item"><input type="checkbox" id="rab">Место работы</li>
      <li class="list-group-item"><input type="checkbox" id="prof">Профессия</li>
      <li class="list-group-item"><input type="checkbox" id="r_n">Социальный статус</li>
      <li class="list-group-item"><input type="checkbox" id="in_t">Категория льготности</li>
      <li class="list-group-item"><input type="checkbox" id="lpy">Кем направлен</li>
      <li class="list-group-item"><input type="checkbox" id="npr_num">№ Направления</li>
      <li class="list-group-item"><input type="checkbox" id="npr_date">Дата направления</li>
      <li class="list-group-item"><input type="checkbox" id="alg">Подозрениена опьянение</li>
      <li class="list-group-item"><input type="checkbox" id="goc">Госпитализация</li>
      <li class="list-group-item"><input type="checkbox" id="prpg">Обращения</li>
      <li class="list-group-item"><input type="checkbox" id="vrez">Давность заболевания</li>
      <li class="list-group-item"><input type="checkbox" id="p_per">Признак поступления</li>
      <li class="list-group-item"><b>Сведения о диагнозах</b></li>
      <li class="list-group-item"><input type="checkbox" id="dsny">Ds направив.учреждения</li>
      <li class="list-group-item"><input type="checkbox" id="ds_0">Ds при поступлении</li>
      <li class="list-group-item"><input type="checkbox" id="dsk">Ds Клинический</li>
      <li class="list-group-item"><input type="checkbox" id="dskz">Ds Клин.заключ</li>
      <li class="list-group-item"><input type="checkbox" id="ds_osl">Ds осложнения</li>
      <li class="list-group-item"><input type="checkbox" id="dsc">Ds сопутствующий</li>
      <li class="list-group-item"><input type="checkbox" id="dson">Ds онкологий</li>
      <li class="list-group-item"><input type="checkbox" id="dat_otd">отметка о дате поступления из приемного отд.</li>
      <li class="list-group-item"><input type="checkbox" id="tm_otd_d">отметка о времени поступления из приемного отд.</li>
      <li class="list-group-item"><input type="checkbox" id="icx">Исход лечения.</li>
      <li class="list-group-item"><input type="checkbox" id="rslt">Результат лечения.</li>
      <li class="list-group-item"><b>Койко-дни</b></li>
      <li class="list-group-item"><input type="checkbox" id="koy_N">Всего койко-дни</li>
      <li class="list-group-item"><input type="checkbox" id="koy_aro">В Аро</li>
      <li class="list-group-item"><input type="checkbox" id="koy_otd">В профильном отделении</li>
      <li class="list-group-item"><input type="checkbox" id="koy_prof_k">Отделение</li>
      <li class="list-group-item"><input type="checkbox" id="koy_kod">Код врача</li>
      <li class="list-group-item"><b>Операции</b></li>
      <li class="list-group-item"><input type="checkbox" id="oper_date">Дата операции</li>
      <li class="list-group-item"><input type="checkbox" id="oper_tm">Время операции</li>
      <li class="list-group-item"><input type="checkbox" id="oper_py">ПО/СТАЦ</li>
      <li class="list-group-item"><input type="checkbox" id="oper_kod_op">Код операции</li>
      <li class="list-group-item"><input type="checkbox" id="oper_goc">ПЛ/ЭК</li>
      <li class="list-group-item"><input type="checkbox" id="oper_kodx">Код хирурга</li>
      <li class="list-group-item"><input type="checkbox" id="oper_pop">Основ.опер?</li>
      <li class="list-group-item"><input type="checkbox" id="oper_pr_osob">Особ-ти операции</li>
      <li class="list-group-item"><input type="checkbox" id="oper_k_mm">К-во.биом</li>
      <li class="list-group-item"><input type="checkbox" id="oper_kodxa">1-Ассистент</li>
      <li class="list-group-item"><input type="checkbox" id="oper_kodxa1">2-Ассистент</li>
      <li class="list-group-item"><input type="checkbox" id="oper_obz">Метод.обез-я</li>
      <li class="list-group-item"><input type="checkbox" id="oper_kodan">Анестезиолог</li>
      <li class="list-group-item"><b>Клинико-стат.гр.заболев-я</b></li>
      <li class="list-group-item"><input type="checkbox" id="ksg_osn">КСГ осн.заболевания</li>
      <li class="list-group-item"><input type="checkbox" id="oopkk">Дополнительный классификатор критерии</li>
      <li class="list-group-item"><input type="checkbox" id="ksg_sop">КСГ сопут.заболевания</li>
      <li class="list-group-item"><input type="checkbox" id="iddoc">Таб.N врача для ОМС</li>
      <li class="list-group-item"><b>Осложнение</b></li>
      <li class="list-group-item"><input type="checkbox" id="oslo_tnvr">Таб.N</li>
      <li class="list-group-item"><input type="checkbox" id="oslo_date">Дата осложнения</li>
      <li class="list-group-item"><input type="checkbox" id="oslo_kod_osl">Код осложнения</li>
      <li class="list-group-item"><input type="checkbox" id="oslo_xosl">Характер осл.</li>
      <li class="list-group-item"><input type="checkbox" id="oslo_posl">Причина</li>
      <li class="list-group-item"><input type="checkbox" id="oslo_aosl">Экспертиза</li>
      <li class="list-group-item"><b>Трудоспособность</b></li>
      <li class="list-group-item"><input type="checkbox" id="trs">Трудоспособность</li>
      <li class="list-group-item"><b>Манипуляция</b></li>
      <li class="list-group-item"><input type="checkbox" id="man_date">Дата манипуляции</li>
      <li class="list-group-item"><input type="checkbox" id="man_tnvr">Таб.N врача</li>
      <li class="list-group-item"><input type="checkbox" id="man_kodmn">Код Манипуляции</li>
      <li class="list-group-item"><input type="checkbox" id="man_kol">К-во</li>
      <li class="list-group-item"><input type="checkbox" id="man_pl">Плат.Услуга?</li>
      <li class="list-group-item"><b>Переводы</b></li>
      <li class="list-group-item"><input type="checkbox" id="potd">Перевод из Отд.</li>
      <li class="list-group-item"><input type="checkbox" id="dat_pe">Дата перевода</li>
      <li class="list-group-item"><input type="checkbox" id="kod_y">Перевод в Др.ЛПУ</li>
      <li class="list-group-item"><input type="checkbox" id="pr_per">Причина перевода</li>
      <li class="list-group-item"><b>Патанатомический Ds</b></li>
      <li class="list-group-item"><input type="checkbox" id="wskr_date">Дата смерти</li>
      <li class="list-group-item"><input type="checkbox" id="tm_let">Время смерти (час.мин)</li>
      <li class="list-group-item"><input type="checkbox" id="pri">Код причины летального исхода</li>
      <li class="list-group-item"><input type="checkbox" id="ds_let_kod">Ds причины летального исхода </li>
      <li class="list-group-item"><input type="checkbox" id="wskr">Вскрытие</li>
      <li class="list-group-item"><input type="checkbox" id="dspat_kod">Ds паталогоанатомический</li>
      <li class="list-group-item"><input type="checkbox" id="rasxp">Расхождение Ds установлено</li>
      <li class="list-group-item"><input type="checkbox" id="otd_y">Умер в</li>
      <li class="list-group-item"><b>Сведения о травмах</b></li>
      <li class="list-group-item"><input type="checkbox" id="dskz_kod">Характер травмы</li>
      <li class="list-group-item"><input type="checkbox" id="details_kod">Внешние причины травмы</li>
      <li class="list-group-item"><input type="checkbox" id="t_trv">Тип травмы</li>
      <li class="list-group-item"><input type="checkbox" id="trav_ns">Травма получена в рез-те противоправных действий третьих лиц</li>
      <li class="list-group-item"><b>Полис/Документ/Снилс</b></li>
      <li class="list-group-item"><input type="checkbox" id="vds">Источник оплаты</li>
      <li class="list-group-item"><input type="checkbox" id="sctp">Сер.полиса</li>
      <li class="list-group-item"><input type="checkbox" id="nctp">N полиса</li>
      <li class="list-group-item"><input type="checkbox" id="ctkom">СМО</li>
      <li class="list-group-item"><input type="checkbox" id="t_pol">Тип полиса</li>
      <li class="list-group-item"><input type="checkbox" id="udl">Тип документа</li>
      <li class="list-group-item"><input type="checkbox" id="s_pasp">Сер.ДУЛ</li>
      <li class="list-group-item"><input type="checkbox" id="n_pasp">N ДУЛ</li>
      <li class="list-group-item"><input type="checkbox" id="docdate">Дата выдачи</li>
      <li class="list-group-item"><input type="checkbox" id="docorg">Кем выдан</li>
      <li class="list-group-item"><input type="checkbox" id="m_roj">Место рождения</li>
      <li class="list-group-item"><input type="checkbox" id="ss">Снилс</li>
      <li class="list-group-item"><b>Сведения о беременности</b></li>
      <li class="list-group-item"><input type="checkbox" id="vb_a_datv">Дата</li>
      <li class="list-group-item"><input type="checkbox" id="srber">Срок беременности (недель)</li>
      <li class="list-group-item"><input type="checkbox" id="n_ber">Настоящая беременность по счету</li>
      <li class="list-group-item"><input type="checkbox" id="pria">Причины прерывания беременности</li>
      <li class="list-group-item"><input type="checkbox" id="m_prer">Метод прерывания беременности</li>
      <li class="list-group-item"><b>Лист нетрудоспособности</b></li>
      <li class="list-group-item"><input type="checkbox" id="dat_l1">Открыт с</li>
      <li class="list-group-item"><input type="checkbox" id="dat_l2">Закрыт по</li>
      <li class="list-group-item"><input type="checkbox" id="ot_ln">Закрыт</li>
      <li class="list-group-item"><input type="checkbox" id="vs_bol">Полных лет</li>
      <li class="list-group-item"><input type="checkbox" id="dis_sex_bol">Пол</li>
      <li class="list-group-item"><b>Представитель пациента</b></li>
      <li class="list-group-item"><input type="checkbox" id="fam_p">Фимилия</li>
      <li class="list-group-item"><input type="checkbox" id="im_p">Имя</li>
      <li class="list-group-item"><input type="checkbox" id="ot_p">Отчество</li>
      <li class="list-group-item"><input type="checkbox" id="pol_p">Пол</li>
      <li class="list-group-item"><input type="checkbox" id="mp_roj">Место рождения</li>
      <li class="list-group-item"><input type="checkbox" id="udl_p">Тип документа</li>
      <li class="list-group-item"><input type="checkbox" id="sp_pasp">Серия</li>
      <li class="list-group-item"><input type="checkbox" id="np_pasp">Номер</li>
      <li class="list-group-item"><input type="checkbox" id="skom_p">СМО</li>
      <li class="list-group-item"><input type="checkbox" id="stat_p">Тип полиса</li>
      <li class="list-group-item"><input type="checkbox" id="s_pol">Сер.полиса</li>
      <li class="list-group-item"><input type="checkbox" id="n_pol">N.полиса</li>
      <li class="list-group-item"><b>Карта онкобольного</b></li>
      <li class="list-group-item"><input type="checkbox" id="ds1_t">Повод обращения</li>
      <li class="list-group-item"><input type="checkbox" id="stad">Стадия заболевания</li>
      <li class="list-group-item"><input type="checkbox" id="onk_t">Стадия по T</li>
      <li class="list-group-item"><input type="checkbox" id="onk_n">Стадия по N</li>
      <li class="list-group-item"><input type="checkbox" id="onk_m">Стадия по M</li>
      <li class="list-group-item"><input type="checkbox" id="mtstz">Наличие отдельных метастазов</li>
      <li class="list-group-item"><input type="checkbox" id="c_zab">Характер заболевания</li>
      <li class="list-group-item"><b>Сведения о диагностике</b></li>
      <li class="list-group-item"><input type="checkbox" id="diag_date">Дата взятия материала</li>
      <li class="list-group-item"><input type="checkbox" id="diag_tip">Тип диагностического показателя</li>
      <li class="list-group-item"><input type="checkbox" id="diag_code">Код диагностического показателя</li>
      <li class="list-group-item"><input type="checkbox" id="diag_rslt">Код результата диагностики</li>
      <li class="list-group-item"><input type="checkbox" id="rec_rslt">Признак получения результата диагностики</li>
      <li class="list-group-item"><b>Сведения о проведении консилиума</b></li>
      <li class="list-group-item"><input type="checkbox" id="dt_cons">Дата консилиума</li>
      <li class="list-group-item"><input type="checkbox" id="pr_cons">Цель консилиума</li>
      <li class="list-group-item"><b>Сведения об услуге лечения</b></li>
      <li class="list-group-item"><input type="checkbox" id="usl_tip">Тип услуги</li>
      <li class="list-group-item"><input type="checkbox" id="hir_tip">Тип хирургического лечения</li>
      <li class="list-group-item"><b>Сведения о противопоказаниях и отказах</b></li>
      <li class="list-group-item"><input type="checkbox" id="d_prot">Дата регистрации</li>
      <li class="list-group-item"><input type="checkbox" id="prot">противопоказания и отказы</li>
      <li class="list-group-item"><b>Сведения о направлений в МО (из выписного эпикриза)</b></li>
      <li class="list-group-item"><input type="checkbox" id="naprdate">Дата направления</li>
      <li class="list-group-item"><input type="checkbox" id="napr_v">Вид направления</li>
      <li class="list-group-item"><input type="checkbox" id="napr_mo">Мо,куда рекомендовано обращаться</li>
      <li class="list-group-item"><input type="checkbox" id="napr_issl">Метод диагностич.исследования</li>
      <li class="list-group-item"><input type="checkbox" id="napr_usl">Мед.услуга(код) рекомендованная</li>
      <li class="list-group-item"><b>Мо прикрепления</b></li>
      <li class="list-group-item"><input type="checkbox" id="pmg">Мо прикрепления</li>
    </ul>
  </div>`
})


Vue.component('input_select', {
    template: `<div>
    <input type="text" v-bind:list="ll" v-bind:id="id" style="margin-bottom: 10px;" class="text-center" :name="n">
    <datalist v-bind:id="ll">
    <option v-for="s in spravlist">{{s[k]}}</option>
    </datalist>
    </div>`,
    props: ['spravlist', 'k', 'll', 'id', 'n']

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

Vue.component('otdel_filter', {
    template: `
        <div id="v_otdel_filter" style="display: none">
            <ul>
                <li v-for="ot in report_oth.$data.sprav_list.Otde" class="list-group-item">
                <input type="checkbox" :value="ot.naim">
                    {{ot.naim}}
                </li>
            </ul>
        </div>
    `
})

let report_oth = new Vue({

    el: '#report_oth',
    data: {
        lists_references: false,
        annual_reports: false,
        menu_list: false,
        menu_group: false,
        menu_annual: false,
        menu_annual_bol: false,
        menu_reports: false,
        report_generation: false,
        v_otdel_filter: false,
        //Справочники
        sprav_list: [],
        otdel: false,

        //Отчеты


        g_tip_ot_3_2_v: false,
        gla_vra: false,
        isfin_l: false,


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



        a_oth_2_select_2_f: false,

        statistics_reports: false,
        departments_reports: false,
        vra_reports: false,
        vault_otd_reports: false,

        statistics_rep_oth_13_1: false,
        statistics_rep_oth_14_1: false,
        statistics_rep_oth_14_2: false,
        statistics_rep_oth_14_3: false,
        statistics_rep_oth_14_4: false,
        statistics_rep_oth_30_1: false,
        statistics_rep_oth_30_2: false,
        statistics_rep_oth_30_3: false,
        statistics_rep_oth_16_1: false,
        statistics_rep_oth_57_1: false,
        statistics_rep_oth_1_1: false,
        statistics_rep_oth_1_2: false,
        statistics_rep_oth_1_3: false,
        statistics_rep_oth_1_4: false,
        statistics_rep_oth_1_5: false,
        statistics_rep_oth_1_6: false,
        statistics_rep_oth_1_7: false,
        statistics_rep_oth_1_8: false,
        statistics_rep_oth_1_9: false,
        statistics_rep_oth_1_а: false,
        statistics_rep_oth_1_б: false,
        statistics_rep_oth_1_в: false,
        statistics_rep_oth_1_г: false,
        statistics_rep_oth_1_д: false,


        shaping: false,
        create: false,
        annual_shaping: false,
        annual_create: false,
        group_st_ot: false,
        group_podly_ternerprof: false,
        group_goc_filt: false,
        m_filter: false,
        group_shaping: false,
        group_create: false,
        group_shaping_a_oth: false,
        group_create_a_oth: false,
        group_error: false,

        panel_m_1: false,
        panel_m_2: false,
        panel_m_3: false,
        panel_m_4: false,
        panel_m_5: false,
        panel_m_6: false,
        panel_m_7: false,
        panel_m_8: false,
        panel_m_9: false,
        panel_m_10: false,
        panel_m_11: false,
        panel_m_12: false,
        panel_m_13: false,
        panel_m_14: false,
        panel_m_15: false,
        panel_m_16: false,
        panel_m_17: false,
        panel_m_18: false,
        panel_m_19: false,
        panel_m_20: false,
        panel_m_21: false,
        panel_m_22: false,
        panel_m_23: false,
        panel_m_24: false,
        panel_m_25: false,
        panel_m_26: false,
        panel_m_27: false,
        panel_m_28: false,
        panel_m_29: false,
        panel_m_30: false,
        panel_m_31: false,
        panel_m_32: false,
        panel_m_33: false,
        select_vault_otd_8: false,
        select_vault_otd_9: false


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
              },
         VraListKodName{
         kod,naim
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
            this.menu_annual_bol = false
            this.menu_reports = false
            this.report_generation = false

            this.group_shaping = false
            this.group_create = false
            this.group_shaping_a_oth = false
            this.group_create_a_oth = false
            this.group_error = false


        },
        init_oth: function () {
            this.otdel = false

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


            this.statistics_reports = false
            this.departments_reports = false
            this.vra_reports = false
            this.vault_otd_reports = false

            this.statistics_rep_oth_1 = false
            this.statistics_rep_oth_2 = false
            this.statistics_rep_oth_3 = false
            this.statistics_rep_oth_4 = false
            this.statistics_rep_oth_5 = false
            this.statistics_rep_oth_6 = false
            this.statistics_rep_oth_7 = false
            this.statistics_rep_oth_8 = false
            this.statistics_rep_oth_9 = false
            this.statistics_rep_oth_10 = false

            this.shaping = false
            this.create = false
            this.annual_shaping = false
            this.annual_create = false

            this.group_shaping = false
            this.group_create = false
            this.group_error = false

            let date_1 = document.getElementById("date1")
            let date_2 = document.getElementById("date2")

            if (date_1 != null) { date_1.value = '' }
            if (date_2 != null) { date_2.value = '' }
            this.m_filter = false

            this.select_vault_otd_8 = false
            this.select_vault_otd_9 = false

        },
        references: function () {
            this.init()
            this.init_oth()
            this.statistics_r_oth_init()
            this.lists_references = !this.lists_references
            this.annual_reports = false
            this.menu_reports = false
            this.menu_group = false
            this.menu_annual = false
            this.menu_annual_bol = false


        },
        reports: function () {
            this.init()
            this.init_oth()
            this.statistics_r_oth_init()

            this.annual_reports = !this.annual_reports
            this.lists_references = false
            this.menu_group = false
            this.menu_annual = false
            this.menu_annual_bol = false
            this.report_generation = false
            this.menu_reports = false

        },
        group: function () {
            this.init_oth()
            this.menu_group = !this.menu_group
            this.menu_annual = false
            this.menu_annual_bol = false

            setTimeout(() => {
                all_filters()
            }, 300)
        },
        annual: function () {
            this.init_oth()
            this.menu_annual = !this.menu_annual
            this.menu_group = false
            this.menu_annual_bol = false

            this.annual_init()
            // this.panel_m_1 = true
        },
        annual_init: function () {
            this.panel_m_1 = false
            this.panel_m_2 = false
            this.panel_m_3 = false
            this.panel_m_4 = false
            this.panel_m_5 = false
            this.panel_m_6 = false
            this.panel_m_7 = false
            this.panel_m_8 = false
            this.panel_m_9 = false
            this.panel_m_10 = false
            this.panel_m_11 = false
            this.panel_m_12 = false
            this.panel_m_13 = false
            this.panel_m_14 = false
            this.panel_m_15 = false
            this.panel_m_16 = false
            this.panel_m_17 = false
            this.panel_m_18 = false
            this.panel_m_19 = false
            this.panel_m_20 = false
            this.panel_m_21 = false
            this.panel_m_22 = false
            this.panel_m_23 = false
            this.panel_m_24 = false
            this.panel_m_25 = false
            this.panel_m_26 = false
            this.panel_m_27 = false
            this.panel_m_28 = false
            this.panel_m_29 = false
            this.panel_m_30 = false
            this.panel_m_31 = false
            this.panel_m_32 = false
            this.panel_m_33 = false
        },
        annual_bol: function () {
            this.init_oth()
            this.menu_annual_bol = !this.menu_annual_bol
            this.menu_group = false
            this.menu_annual = false

        },
        generation: function () {
            this.init_oth()
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
            setTimeout(() => {
                all_filters()
            }, 300)
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
        },
        statistics_rep: function () {

            this.init_oth()
            this.statistics_reports = !this.statistics_reports
            $("#statistics_rep_download").empty()


            // setTimeout(() => {
            //     let panel_13 = document.getElementById("panel_13")

            //     panel_13.onclick = function(){
            //        let menu = document.getElementById("panel-13-menu")
            //        if (menu.classList.contains('show')){
            //            document.getElementById("13-menu").click()
            //        }
            //     }
            // }, 300)


        },
        departments_rep: function () {
            this.init_oth()
            this.departments_reports = !this.departments_reports
            setTimeout(() => {
                document.getElementById("otdel").style = "width:-moz-available;text-align: center;"
            }, 300)

        },
        departments_rep_onchange: function (event) {
            let val = event.target.value
            let btn = document.getElementById("vault_otd_btn")
            btn.setAttribute('n', val)

            if (val == '8'){
                report_oth.$data.select_vault_otd_8 = true
            }
            else{
                report_oth.$data.select_vault_otd_8 = false
            }


            if (val == '9'){
                report_oth.$data.select_vault_otd_9 = true
            }
            else{
                report_oth.$data.select_vault_otd_9 = false
            }

        },
        vra_rep: function () {
            this.init_oth()
            this.vra_reports = !this.vra_reports
            setTimeout(() => {
                vra_rep()
                document.getElementById("vra_n_k").style = "width:-moz-available;text-align: center;"
            }, 300)
            // let vra_list = document.getElementById("vra_kod_naim")
            // vra_list.innerHTML = ""
            // for (d of this.sprav_list.VraListKodName){
            //     let op = document.createElement("option")
            //     op.value = p.kod
            //     vra_list.appendChild(op)
            // }
            // console.log(this.sprav_list.VraListKodName)
        },
        vault_otd_rep: function () {
            this.init_oth()
            this.vault_otd_reports = !this.vault_otd_reports
            // document.getElementById("otd_reports_onchange").onchange = function(event){
            //     console.log(event)
            // }
        },
        statistics_r_oth_init: function () {
            this.statistics_rep_oth_13_1 = false
            this.statistics_rep_oth_14_1 = false
            this.statistics_rep_oth_14_2 = false
            this.statistics_rep_oth_14_3 = false
            this.statistics_rep_oth_14_4 = false
            this.statistics_rep_oth_30_1 = false
            this.statistics_rep_oth_30_2 = false
            this.statistics_rep_oth_30_3 = false
            this.statistics_rep_oth_16_1 = false
            this.statistics_rep_oth_57_1 = false
            this.statistics_rep_oth_1_1 = false
            this.statistics_rep_oth_1_2 = false
            this.statistics_rep_oth_1_3 = false
            this.statistics_rep_oth_1_4 = false
            this.statistics_rep_oth_1_5 = false
            this.statistics_rep_oth_1_6 = false
            this.statistics_rep_oth_1_7 = false
            this.statistics_rep_oth_1_8 = false
            this.statistics_rep_oth_1_9 = false
            this.statistics_rep_oth_1_а = false
            this.statistics_rep_oth_1_б = false
            this.statistics_rep_oth_1_в = false
            this.statistics_rep_oth_1_г = false
            this.statistics_rep_oth_1_д = false
            this.m_filter = false
        },
        statistics_r_oth_13_1: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_13_1 = !this.statistics_rep_oth_13_1
        },
        statistics_r_oth_14_1: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_14_1 = !this.statistics_rep_oth_14_1
        },
        statistics_r_oth_14_2: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_14_2 = !this.statistics_rep_oth_14_2
        },
        statistics_r_oth_14_3: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_14_3 = !this.statistics_rep_oth_14_3
        },
        statistics_r_oth_14_4: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_14_4 = !this.statistics_rep_oth_14_4
        },
        statistics_r_oth_30_1: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_30_1 = !this.statistics_rep_oth_30_1
        },
        statistics_r_oth_30_2: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_30_2 = !this.statistics_rep_oth_30_2
        },
        statistics_r_oth_33_3: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_33_3 = !this.statistics_rep_oth_33_3
        },
        statistics_r_oth_16_1: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_16_1 = !this.statistics_rep_oth_16_1
        },
        statistics_r_oth_57_1: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_57_1 = !this.statistics_rep_oth_57_1
        },
        statistics_r_oth_1_1: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_1_1 = !this.statistics_rep_oth_1_1
        },
        statistics_r_oth_1_2: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_1_2 = !this.statistics_rep_oth_1_2
        },
        statistics_r_oth_1_3: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_1_3 = !this.statistics_rep_oth_1_3
        },
        statistics_r_oth_1_4: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_1_4 = !this.statistics_rep_oth_1_4
        },
        statistics_r_oth_1_5: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_1_5 = !this.statistics_rep_oth_1_5
        },
        statistics_r_oth_1_6: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_1_6 = !this.statistics_rep_oth_1_6
        },
        statistics_r_oth_1_7: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_1_7 = !this.statistics_rep_oth_1_7
        },
        statistics_r_oth_1_8: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_1_8 = !this.statistics_rep_oth_1_8
        },
        statistics_r_oth_1_9: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_1_9 = !this.statistics_rep_oth_1_9
        },
        statistics_r_oth_1_а: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_1_а = !this.statistics_rep_oth_1_а
        },
        statistics_r_oth_1_б: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_1_б = !this.statistics_rep_oth_1_б
        },
        statistics_r_oth_1_в: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_1_в = !this.statistics_rep_oth_1_в
        },
        statistics_r_oth_1_г: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_1_г = !this.statistics_rep_oth_1_г
        },
        statistics_r_oth_1_д: function () {
            this.statistics_r_oth_init()
            this.statistics_rep_oth_1_д = !this.statistics_rep_oth_1_д
        },

        panel_m_filter: function () {
            if (this.m_filter != true) {
                this.m_filter = true
                all_filters()
            }
        },

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

    if (event.target.value == 'Для зам.гл.врача') {
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


function onchange_a_oth_2_select_1(event) {
    if (event.target.value == 'По территор.признаку') {
        report_oth.$data.a_oth_2_select_2_f = true
    }
    else {
        report_oth.$data.a_oth_2_select_2_f = false
    }
}



function onchange_group_p_list_a_oth() {
    report_oth.$data.group_shaping = false
    report_oth.$data.group_create = false
    report_oth.$data.group_error = false
    $("#download_a_oth").empty()


    let val = event.target.value
    report_oth.annual_init()
    if (val == 'a_oth_1') {
        report_oth.$data.panel_m_1 = true
        setTimeout(() => {
            document.getElementById("abobsh").style = "width:-moz-available;text-align: center;"
            document.getElementById("vra").style = "width:-moz-available;text-align: center;"
            document.getElementById("otdel").style = "width:-moz-available;text-align: center;"
            document.getElementById("fam_pat").style = "width:-moz-available;text-align: center;"
            document.getElementById("agegroup").style = "width:-moz-available;text-align: center;"
            document.getElementById("v014").style = "width:-moz-available;text-align: center;"
            document.getElementById("prpg").style = "width:-moz-available;text-align: center;"
            document.getElementById("v005").style = "width:-moz-available;text-align: center;"
            document.getElementById("v012").style = "width:-moz-available;text-align: center;"
        }, 300)
    }
    else if (val == 'a_oth_2') {
        report_oth.$data.panel_m_2 = true
    }
    else if (val == 'a_oth_3') {
        report_oth.$data.panel_m_3 = true
    }
    else if (val == 'a_oth_4') {
        report_oth.$data.panel_m_4 = true
    }
    else if (val == 'a_oth_5') {
        report_oth.$data.panel_m_5 = true
        setTimeout(() => {
            all_filters()
        }, 300)
    }
    else if (val == 'a_oth_6') {
        report_oth.$data.panel_m_6 = true
    }
    else if (val == 'a_oth_7') {
        report_oth.$data.panel_m_7 = true
    }
    else if (val == 'a_oth_8') {
        report_oth.$data.panel_m_8 = true
    }
    else if (val == 'a_oth_9') {
        report_oth.$data.panel_m_9 = true
    }
    else if (val == 'a_oth_10') {
        report_oth.$data.panel_m_10 = true
    }
    else if (val == 'a_oth_11') {
        report_oth.$data.panel_m_11 = true
    }
    else if (val == 'a_oth_11') {
        report_oth.$data.panel_m_11 = true
    }
    else if (val == 'a_oth_12') {
        report_oth.$data.panel_m_12 = true
    }
    else if (val == 'a_oth_13') {
        report_oth.$data.panel_m_13 = true
    }
    else if (val == 'a_oth_14') {
        report_oth.$data.panel_m_14 = true
    }
    else if (val == 'a_oth_15') {
        report_oth.$data.panel_m_15 = true
    }
    else if (val == 'a_oth_16') {
        report_oth.$data.panel_m_16 = true
    }
    else if (val == 'a_oth_17') {
        report_oth.$data.panel_m_17 = true
    }
    else if (val == 'a_oth_18') {
        report_oth.$data.panel_m_18 = true
    }
    else if (val == 'a_oth_19') {
        report_oth.$data.panel_m_19 = true
        setTimeout(() => {
            // document.getElementById("trv").style="width:-moz-available;text-align: center;"
            document.getElementById("trvnas").style = "width:-moz-available;text-align: center;"
        }, 300)

    }
    else if (val == 'a_oth_20') {
        report_oth.$data.panel_m_20 = true
        setTimeout(() => {
            document.getElementById("isfin").style = "width:-moz-available;text-align: center;"
            document.getElementById("v014").style = "width:-moz-available;text-align: center;"
            document.getElementById("f003").style = "width:-moz-available;text-align: center;"
        }, 300)
    }
    else if (val == 'a_oth_21') {
        report_oth.$data.panel_m_21 = true
        setTimeout(() => {
            document.getElementById("a_oth_21_input_1").style = "width:-moz-available;text-align: center;"
            document.getElementById("a_oth_21_input_2").style = "width:-moz-available;text-align: center;"
            document.getElementById("vra").style = "width:-moz-available;text-align: center;"
        }, 300)
    }
    else if (val == 'a_oth_22') {
        report_oth.$data.panel_m_22 = true
    }
    else if (val == 'a_oth_23') {
        report_oth.$data.panel_m_23 = true
    }
    else if (val == 'a_oth_24') {
        report_oth.$data.panel_m_24 = true
    }
    else if (val == 'a_oth_25') {
        report_oth.$data.panel_m_25 = true
    }
    else if (val == 'a_oth_26') {
        report_oth.$data.panel_m_26 = true
    }
    else if (val == 'a_oth_27') {
        report_oth.$data.panel_m_27 = true
        setTimeout(() => {
            document.getElementById("v020").style = "width:-moz-available;text-align: center;"
        }, 300)
    }
    else if (val == 'a_oth_28') {
        report_oth.$data.panel_m_28 = true
    }
    else if (val == 'a_oth_29') {
        report_oth.$data.panel_m_29 = true
    }
    else if (val == 'a_oth_30') {
        report_oth.$data.panel_m_30 = true
    }
    else if (val == 'a_oth_31') {
        report_oth.$data.panel_m_31 = true
    }
    else if (val == 'a_oth_32') {
        report_oth.$data.panel_m_32 = true
    }
    else if (val == 'a_oth_33') {
        report_oth.$data.panel_m_33 = true
    }

}

function all_filters() {
    let list_li = document.getElementById("filters_ul").querySelectorAll('li')
    let filters = document.getElementById("filters")
    let type_lgots = ['Территориальная', 'Федеральная']
    for (let li of list_li) {
        li.firstChild.addEventListener("click", function () {
            let div_block = document.createElement("div")
            div_block.setAttribute("id", this.id + "_block")
            let lab = document.createElement("label")
            lab.innerHTML = this.nextSibling.data
            lab.setAttribute("style", "display:block")
            div_block.appendChild(lab)
            if (this.id == 'datv_filt' || this.id == 'datp_filt' || this.id == 'datv_datp_filt') {
                let dat_1 = document.createElement("input")
                dat_1.setAttribute("type", "date")
                let dat_2 = document.createElement("input")
                dat_2.setAttribute("type", "date")
                let lab_1 = document.createElement("label")
                lab_1.innerHTML = 'C'
                let lab_2 = document.createElement("label")
                lab_2.innerHTML = 'по'
                div_block.appendChild(lab_1)
                div_block.appendChild(dat_1)
                div_block.appendChild(lab_2)
                div_block.appendChild(dat_2)
            }
            else if (this.id == 'otd_filt' || this.id == 'prof_filt' || this.id == 'pol_filt' || this.id == 'type_lgots_filt'
                || this.id == 'in_t_filt' || this.id == 'r_n_filt' || this.id == 'age_group_filt' || this.id == 'goc_filt'
                || this.id == 'prpg_filt' || this.id == 'vrez_filt' || this.id == 'c_oksm_filt' || this.id == 'terr_filt'
                || this.id == 'rai_in_filt' || this.id == 'cj_filt' || this.id == 'lpy_filt' || this.id == 'ctkom_filt'
                || this.id == 'vds_filt' || this.id == 'icx_filt' || this.id == 'otdel_let_filt' || this.id == 'kod_vra_filt'
                || this.id == 'kod_op_filt' || this.id == 'pr_osob_filt' || this.id == 't_trv_filt' || this.id == 'trav_ns_filt'
                || this.id == 'wskr_filt' || this.id == 'rasxp_filt' || this.id == 'potd_filt' || this.id == 'kod_y_filt'
                || this.id == 'pr_per_filt') {

                if (this.id == 'otd_filt' || this.id == 'potd_filt') {
                    var list = report_oth.$data.sprav_list.Otde
                }
                else if (this.id == 'prof_filt') {
                    var list = report_oth.$data.sprav_list.V020
                }
                else if (this.id == 'pol_filt') {
                    var list = report_oth.$data.sprav_list.V005
                }
                else if (this.id == 'type_lgots_filt') {
                    var list = type_lgots
                }
                else if (this.id == 'in_t_filt') {
                    var list = report_oth.$data.sprav_list.T004
                }
                else if (this.id == 'r_n_filt') {
                    var list = report_oth.$data.sprav_list.RabNer
                }
                else if (this.id == 'age_group_filt') {
                    var list = report_oth.$data.sprav_list.AgeGroup
                }
                else if (this.id == 'goc_filt') {
                    var list = report_oth.$data.sprav_list.V014
                }
                else if (this.id == 'prpg_filt') {
                    var list = report_oth.$data.sprav_list.Prpg
                }
                else if (this.id == 'vrez_filt') {
                    var list = report_oth.$data.sprav_list.Vrzb
                }
                else if (this.id == 'c_oksm_filt') {
                    var list = report_oth.$data.sprav_list.Oksm
                }
                else if (this.id == 'terr_filt') {
                    var list = ['г.Тюменю', 'Юг Тюм.обл.кроме Тюм.р-н', 'Тюменский р-н', 'Ханты-Мансйский АО',
                        'Ямало-Немецкий АО', 'Др.регионы Россий', 'Др. государства']
                }
                else if (this.id == 'rai_in_filt') {
                    var list = ['Центральный АО', 'Ленинский АО', 'Калининский АО', 'Восточный АО']
                }
                else if (this.id == 'cj_filt') {
                    var list = ['Городской', 'Сельский']
                }
                else if (this.id == 'lpy_filt' || this.id == 'kod_y_filt') {
                    var list = report_oth.$data.sprav_list.F003
                }
                else if (this.id == 'ctkom_filt') {
                    var list = report_oth.$data.sprav_list.Skom
                }
                else if (this.id == 'vds_filt') {
                    var list = report_oth.$data.sprav_list.Isfin
                }
                else if (this.id == 'icx_filt') {
                    var list = report_oth.$data.sprav_list.V012
                }
                else if (this.id == 'otdel_let_filt') {
                    var list = ['ПРИЕМНОЕ', 'АРО N1', 'АРО 2 ИНТЕН.НЕВРОЛОГ', 'АРО N3 (ЛДО)']
                }
                else if (this.id == 'kod_vra_filt') {
                    var list = report_oth.$data.sprav_list.Vra
                }
                else if (this.id == 'kod_op_filt') {
                    var list = report_oth.$data.sprav_list.V001
                }
                else if (this.id == 'pr_osob_filt') {
                    var list = report_oth.$data.sprav_list.PROsob
                }
                else if (this.id == 't_trv_filt') {
                    var list = report_oth.$data.sprav_list.Trv
                }

                else if (this.id == 'trav_ns_filt') {
                    var list = report_oth.$data.sprav_list.Trvnas
                }

                else if (this.id == 'wskr_filt') {
                    var list = ['без вскрытия', 'патологоанатом.', 'судебное']
                }
                else if (this.id == 'rasxp_filt') {
                    var list = ['да', 'нет']
                }

                else if (this.id == 'pr_per_filt') {
                    var list = ['для оказания специализированной мед.помощи', 'для прохождения реабилитации', 'для следующего этапа лечения']
                }



                let inp = document.createElement("input")
                inp.setAttribute("list", this.id + "_l")
                inp.type = 'text'
                let datalist = document.createElement("datalist")
                datalist.setAttribute("id", this.id + "_l")

                for (o of list) {
                    var op = document.createElement("option")
                    if (this.id == 'otd_filt' || this.id == 'r_n_filt' || this.id == 'prpg_filt'
                        || this.id == 'vrez_filt' || this.id == 'c_oksm_filt' || this.id == 'lpy_filt'
                        || this.id == 'ctkom_filt' || this.id == 'vds_filt' || this.id == 'pr_osob_filt'
                        || this.id == 't_trv_filt' || this.id == 'trav_ns_filt' || this.id == 'potd_filt'
                        || this.id == 'kod_y_filt') {
                        op.value = o.naim
                        op.innerText = o.naim
                    }
                    else if (this.id == 'prof_filt') {
                        op.value = o.kPrname
                        op.innerText = o.kPrname
                    }
                    else if (this.id == 'pol_filt') {
                        op.value = o.polname
                        op.innerText = o.polname
                    }
                    else if (this.id == 'type_lgots_filt' || this.id == 'terr_filt' || this.id == 'rai_in_filt'
                        || this.id == 'cj_filt' || this.id == 'otdel_let_filt' || this.id == 'wskr_filt'
                        || this.id == 'rasxp_filt' || this.id == 'pr_per_filt') {
                        op.value = o
                        op.innerText = o
                    }
                    else if (this.id == 'in_t_filt' || this.id == 'age_group_filt') {
                        op.value = o.name
                        op.innerText = o.name
                    }
                    else if (this.id == 'goc_filt') {
                        op.value = o.tipName
                        op.innerText = o.tipName
                    }
                    else if (this.id == 'icx_filt') {
                        op.value = o.izName
                        op.innerText = o.izName
                    }
                    else if (this.id == 'kod_vra_filt' || this.id == 'kod_op_filt') {
                        op.value = o.kod
                        op.innerText = o.kod
                    }
                    datalist.appendChild(op)
                }
                div_block.appendChild(inp)
                div_block.appendChild(datalist)

            }


            else if (this.id == 'fam_filt' || this.id == 'im_filt' || this.id == 'ot_filt' || this.id == 'dsc_filt'
                || this.id == 'dspat_filt' || this.id == 'dson_filt' || this.id == 'ksg_osn_filt' || this.id == 'reg_obl_rai_filt'
                || this.id == 'dskz_prich_filt' || this.id == 'stay_in_mo_filt' || this.id == 'time_minuts_po_filt' || this.id == 'man_list'
                || this.id == 'metod_hmp' || this.id == 'vid_hmp') {
                let inp = document.createElement("input")
                inp.setAttribute('id', `in_${this.id}`)
                inp.type = 'text'
                div_block.appendChild(inp)
            }
            else if (this.id == 'dskz_filt' || this.id == 'srber_filt') {
                let inp_1 = document.createElement("input")
                inp_1.setAttribute("style", "width:80px")
                let inp_2 = document.createElement("input")
                inp_2.setAttribute("style", "width:80px")
                let lab_1 = document.createElement("label")
                lab_1.innerHTML = 'C'
                let lab_2 = document.createElement("label")
                lab_2.innerHTML = 'по'
                div_block.appendChild(lab_1)
                div_block.appendChild(inp_1)
                div_block.appendChild(lab_2)
                div_block.appendChild(inp_2)
            }

            if (this.checked) {
                filters.appendChild(div_block)
            }
            else {
                filters.removeChild(document.getElementById(this.id + "_block"))
            }


        })
    }
}

function get_checked_filters() {
    var filter = {}
    for (div of filters.childNodes) {
        if (div.id == 'datv_datp_filt') {
            filter.datv_datp = {
                datp: div.childNodes[2].value,
                datv: div.childNodes[4].value
            }
        }
        else if (div.id == 'datv_filt_block') {
            filter.datv = {
                date_1: div.childNodes[2].value,
                date_2: div.childNodes[4].value
            }
        }
        else if (div.id == 'datp_filt_block') {
            filter.datp = {
                date_1: div.childNodes[2].value,
                date_2: div.childNodes[4].value
            }
        }
        else if (div.id == 'otd_filt_block') {
            filter.otd = {
                otd: div.childNodes[1].value,
            }
        }
        else if (div.id == 'prof_filt_block') {
            filter.prof = {
                prof: div.childNodes[1].value,
            }
        }
        else if (div.id == 'fam_filt_block') {
            filter.fam = {
                fam: div.childNodes[1].value,
            }
        }
        else if (div.id == 'im_filt_block') {
            filter.im = {
                im: div.childNodes[1].value,
            }
        }
        else if (div.id == 'ot_filt_block') {
            filter.ot = {
                ot: div.childNodes[1].value,
            }
        }
        else if (div.id == 'pol_filt_block') {
            filter.pol = {
                pol: div.childNodes[1].value,
            }
        }
        else if (div.id == 'type_lgots_filt_block') {
            filter.type_lgots = {
                type_lgots: div.childNodes[1].value,
            }
        }
        else if (div.id == 'in_t_filt_block') {
            filter.in_t = {
                in_t: div.childNodes[1].value,
            }
        }
        else if (div.id == 'r_n_filt_block') {
            filter.r_n = {
                r_n: div.childNodes[1].value,
            }
        }
        else if (div.id == 'age_group_filt_block') {
            filter.age_group = {
                age_group: div.childNodes[1].value,
            }
        }
        else if (div.id == 'goc_filt_block') {
            filter.goc = {
                goc: div.childNodes[1].value,
            }
        }
        else if (div.id == 'prpg_filt_block') {
            filter.prpg = {
                prpg: div.childNodes[1].value,
            }
        }
        else if (div.id == 'vrez_filt_block') {
            filter.vrez = {
                vrez: div.childNodes[1].value,
            }
        }
        else if (div.id == 'dskz_filt_block') {
            filter.dskz = {
                dskz_1: div.childNodes[2].value,
                dskz_2: div.childNodes[4].value
            }
        }
        else if (div.id == 'dsc_filt_block') {
            filter.dsc = {
                dsc: div.childNodes[1].value,
            }
        }
        else if (div.id == 'dspat_filt_block') {
            filter.dspat = {
                dspat: div.childNodes[1].value,
            }
        }
        else if (div.id == 'dson_filt_block') {
            filter.dson = {
                dson: div.childNodes[1].value,
            }
        }
        else if (div.id == 'dson_filt_block') {
            filter.dson = {
                dson: div.childNodes[1].value,
            }
        }
        else if (div.id == 'ksg_osn_filt_block') {
            filter.ksg_osn = {
                ksg_osn: div.childNodes[1].value,
            }
        }
        else if (div.id == 'c_oksm_filt_block') {
            filter.c_oksm = {
                c_oksm: div.childNodes[1].value,
            }
        }
        else if (div.id == 'terr_filt_block') {
            filter.terr = {
                terr: div.childNodes[1].value,
            }
        }
        else if (div.id == 'reg_obl_rai_filt_block') {
            filter.reg = {
                reg: div.childNodes[1].value,
            }
        }
        else if (div.id == 'rai_in_filt_block') {
            filter.rai_in = {
                rai_in: div.childNodes[1].value,
            }
        }
        else if (div.id == 'cj_filt_block') {
            filter.cj = {
                cj: div.childNodes[1].value,
            }
        }
        else if (div.id == 'lpy_filt_block') {
            filter.lpy = {
                lpy: div.childNodes[1].value,
            }
        }
        else if (div.id == 'ctkom_filt_block') {
            filter.ctkom = {
                ctkom: div.childNodes[1].value,
            }
        }
        else if (div.id == 'vds_filt_block') {
            filter.vds = {
                vds: div.childNodes[1].value,
            }
        }
        else if (div.id == 'icx_filt_block') {
            filter.icx = {
                icx: div.childNodes[1].value,
            }
        }
        else if (div.id == 'otdel_let_filt_block') {
            filter.otdel_let = {
                otdel_let: div.childNodes[1].value,
            }
        }
        else if (div.id == 'kod_vra_filt_block') {
            filter.kod_vra = {
                vra: div.childNodes[1].value,
            }
        }
        else if (div.id == 'kod_op_filt_block') {
            filter.kod_op = {
                kod_op: div.childNodes[1].value,
            }
        }
        else if (div.id == 'pr_osob_filt_block') {
            filter.pr_osob = {
                pr_osob: div.childNodes[1].value,
            }
        }
        else if (div.id == 't_trv_filt_block') {
            filter.t_trv = {
                t_trv: div.childNodes[1].value,
            }
        }
        else if (div.id == 'trav_ns_filt_block') {
            filter.trav_ns = {
                trav_ns: div.childNodes[1].value,
            }
        }
        else if (div.id == 'disability_filt_block') {
            filter.disability = {
                disability: div.childNodes[0].value,
            }
        }

        else if (div.id == 'srber_filt_block') {
            filter.srber = {
                num_1: div.childNodes[2].value,
                num2_2: div.childNodes[4].value
            }
        }
        else if (div.id == 'potd_filt_block') {
            filter.potd = {
                potd: div.childNodes[1].value,
            }
        }
        else if (div.id == 'kod_y_filt_block') {
            filter.kod_y = {
                kod_y: div.childNodes[1].value,
            }
        }
        else if (div.id == 'dskz_prich_filt_block') {
            filter.dskz_prich = {
                dskz_prich: div.childNodes[1].value,
            }
        }
        else if (div.id == 'pr_per_filt_block') {
            filter.pr_per = {
                pr_per: div.childNodes[1].value,
            }
        }
        else if (div.id == 'time_minuts_po_filt_block') {
            filter.time_minuts_po = {
                time_minuts_po: div.childNodes[1].value,
            }
        }
        else if (div.id == 'stay_in_mo_filt_block') {
            filter.stay_in_mo = {
                stay_in_mo: div.childNodes[1].value,
            }
        }
        else if (div.id == 'metod_hmp_block') {
            filter.metod_hmp = {
                metod_hmp: div.childNodes[1].value
            }
        }
        else if (div.id == 'vid_hmp_block') {
            filter.vid_hmp = {
                vid_hmp: div.childNodes[1].value
            }
        }
    }

    return { filter }

}

function vra_rep() {
    let vra_list = document.getElementById("vra_kod_naim")
    vra_list.innerHTML = ""
    for (d of report_oth.$data.sprav_list.VraListKodName) {
        let op = document.createElement("option")
        op.value = d.kod + ' ' + d.naim
        vra_list.appendChild(op)
    }
}



function create_reports(event) {
    let type_report = event.target.getAttribute('btn')

    report_oth.$data.group_shaping = true
    report_oth.$data.group_create = false
    report_oth.$data.group_error = false
    $("#group_download").empty()
    $("#download_a_oth").empty()
    $("#statistics_rep_download").empty()


    if (type_report == 'g_oth') { mix_reports() }
    else if (type_report == 'a_oth_1') { a_oth_1_f(type_report) }
    else if (type_report == 'a_oth_2') { a_oth_2_f(type_report) }
    else if (type_report == 'a_oth_3') { a_oth_3_f(type_report) }
    else if (type_report == 'a_oth_4') { a_oth_4_f(type_report) }
    else if (type_report == 'a_oth_5') { a_oth_5_f(type_report) }
    else if (type_report == 'a_oth_6') { a_oth_6_f(type_report) }
    else if (type_report == 'a_oth_7') { a_oth_7_f(type_report) }
    else if (type_report == 'a_oth_8') { a_oth_8_f(type_report) }
    else if (type_report == 'a_oth_9') { a_oth_9_f(type_report) }
    else if (type_report == 'a_oth_10') { a_oth_10_f(type_report) }
    else if (type_report == 'a_oth_11') { a_oth_11_f(type_report) }
    else if (type_report == 'a_oth_12') { a_oth_12_f(type_report) }
    else if (type_report == 'a_oth_13') { a_oth_13_f(type_report) }
    else if (type_report == 'a_oth_14') { a_oth_14_f(type_report) }
    else if (type_report == 'a_oth_15') { a_oth_15_f(type_report) }
    else if (type_report == 'a_oth_16') { a_oth_16_f(type_report) }
    else if (type_report == 'a_oth_17') { a_oth_17_f(type_report) }
    else if (type_report == 'a_oth_18') { a_oth_18_f(type_report) }
    else if (type_report == 'a_oth_19') { a_oth_19_f(type_report) }
    else if (type_report == 'a_oth_20') { a_oth_20_f(type_report) }
    else if (type_report == 'a_oth_21') { a_oth_21_f(type_report) }
    else if (type_report == 'a_oth_22') { a_oth_22_f(type_report) }
    else if (type_report == 'a_oth_23') { a_oth_23_f(type_report) }
    else if (type_report == 'a_oth_24') { a_oth_24_f(type_report) }
    else if (type_report == 'a_oth_25') { a_oth_25_f(type_report) }
    else if (type_report == 'a_oth_26') { a_oth_26_f(type_report) }
    else if (type_report == 'a_oth_27') { a_oth_27_f(type_report) }
    else if (type_report == 'a_oth_28') { a_oth_28_f(type_report) }
    else if (type_report == 'a_oth_29') { a_oth_29_f(type_report) }
    else if (type_report == 'a_oth_30') { a_oth_30_f(type_report) }
    else if (type_report == 'a_oth_31') { a_oth_31_f(type_report) }
    else if (type_report == 'a_oth_32') { a_oth_32_f(type_report) }
    else if (type_report == 'a_oth_33') { a_oth_33_f(type_report) }
    else if (type_report == 'annual_13_1_1') { annual_13_1_1_f(type_report) }
    else if (type_report == 'annual_13_1_2') { annual_13_1_2_f(type_report) }
    else if (type_report == 'annual_13_1_3') { annual_13_1_3_f(type_report) }
    else if (type_report == 'annual_13_1_4') { annual_13_1_4_f(type_report) }
    else if (type_report == 'annual_13_1_5') { annual_13_1_5_f(type_report) }
    else if (type_report == 'annual_14_1_1') { annual_14_1_1_f(type_report) }
    else if (type_report == 'annual_14_1_2') { annual_14_1_2_f(type_report) }
    else if (type_report == 'annual_14_1_3') { annual_14_1_3_f(type_report) }
    else if (type_report == 'annual_14_1_4') { annual_14_1_4_f(type_report) }
    else if (type_report == 'annual_14_1_5') { annual_14_1_5_f(type_report) }
    else if (type_report == 'annual_14_2_1') { annual_14_2_1_f(type_report) }
    else if (type_report == 'annual_14_3_1') { annual_14_3_1_f(type_report) }
    else if (type_report == 'annual_14_3_2') { annual_14_3_2_f(type_report) }
    else if (type_report == 'annual_14_3_3') { annual_14_3_3_f(type_report) }
    else if (type_report == 'annual_14_3_4') { annual_14_3_4_f(type_report) }
    else if (type_report == 'annual_14_3_5') { annual_14_3_5_f(type_report) }
    else if (type_report == 'annual_14_3_6') { annual_14_3_6_f(type_report) }
    else if (type_report == 'annual_14_3_7') { annual_14_3_7_f(type_report) }
    else if (type_report == 'annual_14_3_8') { annual_14_3_8_f(type_report) }
    else if (type_report == 'annual_30_1_1') { annual_30_1_1_f(type_report) }
    else if (type_report == 'annual_30_2_1') { annual_30_2_1_f(type_report) }
    else if (type_report == 'annual_30_2_2') { annual_30_2_2_f(type_report) }
    else if (type_report == 'annual_30_2_3') { annual_30_2_3_f(type_report) }
    else if (type_report == 'annual_30_3_1') { annual_30_3_1_f(type_report) }
    else if (type_report == 'annual_16_1_1') { annual_16_1_1_f(type_report) }
    else if (type_report == 'annual_57_1_1') { annual_57_1_1_f(type_report) }
    else if (type_report == 'annual_57_1_2') { annual_57_1_2_f(type_report) }
    else if (type_report == 'annual_57_1_3') { annual_57_1_3_f(type_report) }
    else if (type_report == 'annual_57_1_4') { annual_57_1_4_f(type_report) }
    else if (type_report == 'annual_pr_1') { annual_pr_1_f(type_report) }
    else if (type_report == 'annual_pr_2') { annual_pr_2_f(type_report) }
    else if (type_report == 'annual_pr_3') { annual_pr_3_f(type_report) }
    else if (type_report == 'annual_pr_4') { annual_pr_4_f(type_report) }
    else if (type_report == 'annual_pr_5') { annual_pr_5_f(type_report) }
    else if (type_report == 'annual_pr_6') { annual_pr_6_f(type_report) }
    else if (type_report == 'annual_pr_7') { annual_pr_7_f(type_report) }
    else if (type_report == 'annual_pr_8') { annual_pr_8_f(type_report) }
    else if (type_report == 'annual_pr_9') { annual_pr_9_f(type_report) }
    else if (type_report == 'annual_pr_a') { annual_pr_a_f(type_report) }
    else if (type_report == 'annual_pr_b') { annual_pr_b_f(type_report) }
    else if (type_report == 'annual_pr_v') { annual_pr_v_f(type_report) }
    else if (type_report == 'annual_pr_g') { annual_pr_g_f(type_report) }
    else if (type_report == 'annual_pr_d') { annual_pr_d_f(type_report) }
    else if (type_report == 'annual_vra') { annual_pr_vra(type_report) }

    else if ('departments_rep'.indexOf(type_report) == -1) { departments_rep(type_report) }
    // else if (type_report == 'departments_rep_2') { departments_rep_2(type_report) }
    // else if (type_report == 'departments_rep_3') { departments_rep_3(type_report) }
    // else if (type_report == 'departments_rep_4') { departments_rep_4(type_report) }
    // else if (type_report == 'departments_rep_5') { departments_rep_5(type_report) }
    // else if (type_report == 'departments_rep_6') { departments_rep_6(type_report) }
    // else if (type_report == 'departments_rep_7') { departments_rep_7(type_report) }
    // else if (type_report == 'departments_rep_8') { departments_rep_8(type_report) }
    // else if (type_report == 'departments_rep_9') { departments_rep_9(type_report) }
    // else if (type_report == 'departments_rep_a') { departments_rep_a(type_report) }
    // else if (type_report == 'departments_rep_b') { departments_rep_b(type_report) }
    // else if (type_report == 'departments_rep_v') { departments_rep_v(type_report) }
    // else if (type_report == 'departments_rep_g') { departments_rep_g(type_report) }
    // else if (type_report == 'departments_rep_d') { departments_rep_d(type_report) }


}
function mix_reports() {
    $("#download").empty()
    report_oth.$data.annual_shaping = false
    report_oth.$data.annual_create = true
    let filters = get_checked_filters()
    let list_data = get_checked_input(document.getElementById("list_data"))
    let date_1 = document.getElementById("date1")
    let date_2 = document.getElementById("date2")

    let group_p = document.getElementById("group_p_list")
    let group_st_ot = document.getElementById("group_st_ot")

    var formData = new FormData()
    formData.append('task_type', 'kcc_cb')
    formData.append('date_1', date_1.value)
    formData.append('date_2', date_2.value)
    formData.append('filters', JSON.stringify(filters))

    formData.append('group_p_list', group_p.value)

    if (group_st_ot != undefined) {
        formData.append('group_st_ot', group_st_ot.value)
    }
    else {
        formData.append('group_st_ot', '')
    }

    if (list_data.length > 0) {
        formData.append('list_data', JSON.stringify(list_data))
    }

    formData.append('otdels', JSON.stringify(get_otdel_filter()))

    if (date_1.value != "" && date_2.value != "") {
        sendRequest_f(formData)
    }
}
function a_oth_1_f(type_report) {
    let date_1 = $("#panel_m-1").find("#date1")
    let date_2 = $("#panel_m-1").find("#date2")
    let abobsh = document.getElementById("abobsh")
    let vra = document.getElementById("vra")
    let otdel = document.getElementById("otdel")
    let fam_pat = document.getElementById("fam_pat")
    let agegroup = document.getElementById("agegroup")
    let v014 = document.getElementById("v014")
    let prpg = document.getElementById("prpg")
    let v005 = document.getElementById("v005")
    let ds_1 = document.getElementById("input_1")
    let ds_2 = document.getElementById("input_2")
    let v012 = document.getElementById("v012")


    var filter = {}

    filter.abobsh_list = {
        abobsh: abobsh.value
    }
    filter.kod_vra_man = {
        vra: vra.value
    }
    filter.otd = {
        otd: otdel.value
    }
    filter.fam = {
        fam: fam_pat.value
    }
    filter.age_group = {
        age_group: agegroup.value
    }
    filter.goc = {
        goc: v014.value
    }
    filter.prpg = {
        prpg: prpg.value
    }
    filter.pol = {
        pol: v005.value
    }
    filter.dskz = {
        dskz_1: ds_1.value,
        dskz_2: ds_2.value
    }
    filter.icx = {
        icx: v012.value
    }

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    // formData.append("abobsh", abobsh.value)
    // formData.append("vra", vra.value)
    // formData.append("otdel", otdel.value)
    // formData.append("fam_pat", fam_pat.value)
    // formData.append("agegroup", agegroup.value)
    // formData.append("v014", v014.value)
    // formData.append("prpg", prpg.value)
    // formData.append("v005", v005.value)
    // formData.append("ds_1", ds_1.value)
    // formData.append("ds_2", ds_2.value)
    // formData.append("v012", v012.value)
    formData.append('filters', JSON.stringify({ filter }))

    // console.log(date_1.value)
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }

}
function a_oth_2_f(type_report) {
    // let div = document.getElementById("panel_m-2").getElementById("date1")
    // console.log(div.childNodes[0])
    let date_1 = $("#panel_m-2").find("#date1")
    let date_2 = $("#panel_m-2").find("#date2")
    let select_1 = document.getElementById("a_oth_2_select_1")
    let select_2 = document.getElementById("a_oth_2_select_2")


    var filter = {}
    if (select_2 != null) {
        filter.terr = {
            terr: select_2.value
        }
    }

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    formData.append("select_1", select_1.value)
    formData.append("filter", JSON.stringify({ filter }))


    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_3_f(type_report) {
    let date_1 = $("#panel_m-3").find("#date1")
    let date_2 = $("#panel_m-3").find("#date2")
    let select_1 = document.querySelectorAll("select")[0]

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.value)
    formData.append("date_2", date_2.value)
    formData.append("select_1", select_1.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_4_f(type_report) {
    let date_1 = $("#panel_m-4").find("#date1")
    let date_2 = $("#panel_m-4").find("#date2")
    let input = document.getElementById("a_oth_4_ds")


    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    formData.append("input", input.value)

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_5_f(type_report) {
    let filters = get_checked_filters()
    let date_1 = $("#panel_m-5").find("#date1")
    let date_2 = $("#panel_m-5").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    formData.append('filters', JSON.stringify(filters))

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_6_f(type_report) {
    let date_1 = $("#panel_m-6").find("#date1")
    let date_2 = $("#panel_m-6").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_7_f(type_report) {
    let date_1 = $("#panel_m-7").find("#date1")
    let date_2 = $("#panel_m-7").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_8_f(type_report) {
    let date_1 = $("#panel_m-8").find("#date1")
    let date_2 = $("#panel_m-8").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_9_f(type_report) {
    let date_1 = $("#panel_m-9").find("#date1")
    let date_2 = $("#panel_m-9").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_10_f(type_report) {
    let date_1 = $("#panel_m-10").find("#date1")
    let date_2 = $("#panel_m-10").find("#date2")
    let select = document.getElementById("a_oth_10_select")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    formData.append("select", select.value)

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_11_f(type_report) {
    let date_1 = $("#panel_m-11").find("#date1")
    let date_2 = $("#panel_m-11").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_12_f(type_report) {
    let date_1 = $("#panel_m-12").find("#date1")
    let date_2 = $("#panel_m-12").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_13_f(type_report) {
    let date_1 = $("#panel_m-13").find("#date1")
    let date_2 = $("#panel_m-13").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_14_f(type_report) {
    let date_1 = $("#panel_m-14").find("#date1")
    let date_2 = $("#panel_m-14").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_15_f(type_report) {
    let date_1 = $("#panel_m-15").find("#date1")
    let date_2 = $("#panel_m-15").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_16_f(type_report) {
    let date_1 = $("#panel_m-16").find("#date1")
    let date_2 = $("#panel_m-16").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_17_f(type_report) {
    let date_1 = $("#panel_m-17").find("#date1")
    let date_2 = $("#panel_m-17").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_18_f(type_report) {
    let date_1 = $("#panel_m-18").find("#date1")
    let date_2 = $("#panel_m-18").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_19_f(type_report) {
    let date_1 = $("#panel_m-19").find("#date1")
    let date_2 = $("#panel_m-19").find("#date2")
    let trv = document.getElementById("trv")
    let trvnas = document.getElementById("trvnas")


    var filter = {}


    filter.t_trv = {
        t_trv: trv.value,
    }

    filter.trav_ns = {
        trav_ns: trvnas.value,
    }



    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    // formData.append("trv", trv.value)
    // formData.append("trvnas", trvnas.value)
    formData.append("filter", JSON.stringify({ filter }))

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_20_f(type_report) {
    var filter = {}
    filter.vds = {
        vds: $("input[name*='in_Isfin_p_m_20']").val()
    }
    filter.dskz = {
        dskz_1: $("input[name*='dskz1_p_m_20']").val(),
        dskz_2: $("input[name*='dskz2_p_m_20']").val()
    }
    filter.goc = {
        goc: $("input[name*='v014_p_m_20']").val()
    }
    filter.lpy = {
        lpy: $("input[name*='f003_p_m_20']").val()
    }


    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", $("input[name*='dat1_p_m_20']").val())
    formData.append("date_2", $("input[name*='dat2_p_m_20']").val())

    formData.append("filter", JSON.stringify({ filter }))

    if ($("input[name*='dat1_p_m_20']").val() != "" && $("input[name*='dat2_p_m_20']").val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_21_f(type_report) {
    let date_1 = $("#panel_m-21").find("#date1")
    let date_2 = $("#panel_m-21").find("#date2")
    let select = document.getElementById("a_oth_21_select")
    let input_1 = document.getElementById("a_oth_21_input_1")
    let input_2 = document.getElementById("a_oth_21_input_2")
    let vra = document.getElementById("vra")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    formData.append("select", select.value)
    formData.append("input_1", input_1.value)
    formData.append("input_2", input_2.value)
    formData.append("vra", vra.value)


    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }

}
function a_oth_22_f(type_report) {
    let date_1 = $("#panel_m-22").find("#date1")
    let date_2 = $("#panel_m-22").find("#date2")


    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())


    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_23_f(type_report) {
    let date_1 = $("#panel_m-23").find("#date1")
    let date_2 = $("#panel_m-23").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_24_f(type_report) {
    let date_1 = $("#panel_m-24").find("#date1")
    let date_2 = $("#panel_m-24").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_25_f(type_report) {
    let date_1 = $("#panel_m-25").find("#date1")
    let date_2 = $("#panel_m-25").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_26_f(type_report) {
    let date_1 = $("#panel_m-26").find("#date1")
    let date_2 = $("#panel_m-26").find("#date2")
    let select = document.getElementById("a_oth_26_select")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    formData.append("select", select.value)

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_27_f(type_report) {
    let date_1 = $("#panel_m-27").find("#date1")
    let date_2 = $("#panel_m-27").find("#date2")
    let select = document.getElementById("a_oth_27_select")
    let v020 = document.getElementById("v020")


    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    formData.append("select", select.value)
    formData.append("v020", v020.value)


    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }

}
function a_oth_28_f(type_report) {
    let date_1 = $("#panel_m-28").find("#date1")
    let date_2 = $("#panel_m-28").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_29_f(type_report) {
    let date_1 = $("#panel_m-29").find("#date1")
    let date_2 = $("#panel_m-29").find("#date2")
    let input_ds_1 = document.getElementById("input_1")
    let input_ds_2 = document.getElementById("input_2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    formData.append("input_ds_1", input_ds_1.value)
    formData.append("input_ds_2", input_ds_2.value)

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_30_f(type_report) {
    let date_1 = $("#panel_m-30").find("#date1")
    let date_2 = $("#panel_m-30").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_31_f(type_report) {
    let date_1 = $("#panel_m-31").find("#date1")
    let date_2 = $("#panel_m-31").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_32_f(type_report) {
    let date_1 = $("#panel_m-32").find("#date1")
    let date_2 = $("#panel_m-32").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}
function a_oth_33_f(type_report) {
    let date_1 = $("#panel_m-33").find("#date1")
    let date_2 = $("#panel_m-33").find("#date2")

    var formData = new FormData()
    formData.append('task_type', 'reports')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        // report_oth.$data.create = false
        // report_oth.$data.shaping = true
    }
}

function annual_13_1_1_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }

}

function annual_13_1_2_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }

}

function annual_13_1_3_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }

}

function annual_13_1_4_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }

}

function annual_13_1_5_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }

}

function annual_14_1_1_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_14_1_2_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_14_1_3_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_14_1_4_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_14_1_5_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_14_2_1_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_14_3_1_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_14_3_2_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_14_3_3_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_14_3_4_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_14_3_5_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}
function annual_14_3_6_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_14_3_7_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_14_3_8_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_30_1_1_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_30_2_1_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_30_2_2_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_30_2_3_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_30_3_1_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_16_1_1_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_57_1_1_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_57_1_2_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}


function annual_57_1_3_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_57_1_4_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_57_1_5_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_1_f(type_report) {
    console.log('asdasdasd')
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_2_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_3_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_4_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_5_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_6_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_7_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_8_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_9_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_a_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_b_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_v_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_g_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_d_f(type_report) {
    let date_1 = $("#statistics_rep").find("#date1")
    let date_2 = $("#statistics_rep").find("#date2")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function annual_pr_vra(type_report) {
    let date_1 = $("#date1")
    let date_2 = $("#date2")
    let vra = $("#vra_n_k")
    var formData = new FormData()
    formData.append('task_type', 'annual')
    formData.append('type_report', type_report)
    formData.append("date_1", date_1.val())
    formData.append("date_2", date_2.val())
    formData.append("vra", vra.val())

    if (date_1.val() != "" && date_2.val() != "") {
        sendRequest_f(formData)
        report_oth.$data.annual_create = false
        report_oth.$data.annual_shaping = true
    }
}

function departments_rep(type_report) {
    console.log(type_report)
}
// function departments_rep_2(type_report){}
// function departments_rep_3(type_report){}
// function departments_rep_4(type_report){}
// function departments_rep_5(type_report){}
// function departments_rep_6(type_report){}
// function departments_rep_7(type_report){}
// function departments_rep_8(type_report){}
// function departments_rep_9(type_report){}
// function departments_rep_a(type_report){}
// function departments_rep_b(type_report){}
// function departments_rep_v(type_report){}
// function departments_rep_g(type_report){}
// function departments_rep_d(type_report){}

function sendRequest_f(formData) {
    var r = sendRequest('reports/', 'post', formData)
        .then(response => {
            // console.log(response.data.rez)
        })
        .catch(error => {
        })
}

function get_checked_input(ul) {
    if (ul != null && ul != undefined) {
        let list_input = ul.querySelectorAll("input")
        let checked_input = []
        for (input of list_input) {
            if (input.checked) {
                checked_input.push(input.id)
            }
        }
        return checked_input
    }
    return ''

}




function departments_reports() {
}

function vra_reports() {
}

function otd_reports() {
    document.getElementById("select_vault_otd").value = ''
    // if (event.target.value == 'ттт') {
    //     document.getElementById("vault_otd_btn").setAttribute('value', 'ттт')
    // }
    // else if (event.target.value == 'ннн') {
    //     document.getElementById("vault_otd_btn").setAttribute('value', 'ннн')
    // }
    // else {
    //     document.getElementById("vault_otd_btn").setAttribute('value', '')
    // }
}
function on_select_vault_otd() {
    let v = document.getElementById("select_vault_otd").value

    if (v == '8') {
        report_oth.$data.select_vault_otd_8 = true
    }
    else {
        report_oth.$data.select_vault_otd_8 = false
    }

    if (v == '9') {
        report_oth.$data.select_vault_otd_9 = true
    }
    else {
        report_oth.$data.select_vault_otd_9 = false
    }


    document.getElementById("vault_otd_btn").setAttribute('t', document.getElementById("otd_reports_onchange").value)
    document.getElementById("vault_otd_btn").setAttribute('n', document.getElementById("select_vault_otd").value)
}

function vault_otd_reports() {
    let date1 = document.getElementById("date1")
    let date2 = document.getElementById("date2")
    var formData = new FormData()

    let btn = document.getElementById("vault_otd_btn")
    formData.append("date_1", date1.value)
    formData.append("date_2", date2.value)
    formData.append("type", btn.getAttribute("t"))
    formData.append("n", btn.getAttribute("n"))
    formData.append('group_p_list', 'vault_otd_rep')
    formData.append('task_type', 'reports')
    try {
        formData.append('otdel', document.getElementById("otdel").value)
    }
    catch {
        formData.append('otdel', '')
    }

    report_oth.$data.group_shaping = true
    report_oth.$data.group_create = false
    report_oth.$data.group_error = false
    $("#download_vault_otd").empty()

    if (date1.value != "" && date2.value != "") {
        sendRequest_f(formData)
    }


}

function init_list_data(disabled_filters, list_data) {

    let list_input = document.getElementById("list_data").querySelectorAll("input")
    for (i of list_input) {
        i.checked = false
    }
    let filters = document.getElementById("filters_ul").querySelectorAll("input")
    for (f of filters) {
        f.checked = false
    }

    if (disabled_filters) {
        for (d of document.getElementById("filters_ul").querySelectorAll("li")) {
            d.classList.add('disabled')
        }
    }
    else {
        for (d of document.getElementById("filters_ul").querySelectorAll("li")) {
            d.classList.remove('disabled')
        }
    }

    if (list_data) {
        for (d of document.getElementById("list_data").querySelectorAll("li")) {
            d.classList.add('disabled')
        }
    }
    else {
        for (d of document.getElementById("list_data").querySelectorAll("li")) {
            d.classList.remove('disabled')
        }
    }

}

function p_list_cast(h) {
    document.getElementById("filters_ul").setAttribute('style', 'display:none')
    document.getElementById("list_data").setAttribute('style', 'display:none')
    let menu = document.getElementById("menu-annual-reports").getElementsByClassName('col-md-4')
    for (m of menu) {
        m.setAttribute('style', `height: ${h}px;position: static;text-align: center`)
    }

}
function p_list_lit(h) {
    let menu = document.getElementById("menu-annual-reports").getElementsByClassName('col-md-4')
    for (m of menu) {
        m.childNodes[0].setAttribute('style', `height: ${h}px;position: static`)
    }
}

// function width_input_on(){
//     let div = $('#filters')
//     let inp = $('input', div)
//     console.log(inp)
// inp = document.getElementById("filters")
// for (i of inp.childNodes){
//     console.log(i)
// }
// }
// function width_input_off(){}

function onchange_group_p_list() {
    report_oth.$data.group_shaping = false
    report_oth.$data.group_create = false
    report_oth.$data.group_error = false
    // width_input_on()
    // document.getElementById("filters_ul").style.visibility = "visible"
    // document.getElementById("menu-group").style.visibility = "visible"
    $("#group_download").empty()

    on_checked_filter()
    document.getElementById("v_otdel_filter").style = "display: none"
    report_oth.$data.group_st_ot = false
    report_oth.$data.group_podly_ternerprof = false
    report_oth.$data.group_goc_filt = false


    document.getElementById("filters_ul").removeAttribute('style')
    document.getElementById("list_data").removeAttribute('style')
    document.getElementById("an_rep_data").removeAttribute('style')

    let select = document.getElementById("group_p_list")

    let menu = document.getElementById("menu-annual-reports").getElementsByClassName('col-md-4')
    for (m of menu) {
        m.removeAttribute('style')
    }

    if (select.value == 'group_p1') {
        init_list_data(true, true)
        report_oth.$data.group_st_ot = true

        p_list_cast(450)


        // document.getElementById("menu-annual-reports").getElementsByClassName('col-md-4').setAttribute('style','height: 150px;')

        // fl.style.display = 'none'
        // document.getElementById("filters_ul").style.display = "none"
        // document.getElementById("menu-group").style.display = "none"
    }
    else if (select.value == 'group_p2') {
        init_list_data(false, true)
        p_list_lit(450)
        document.getElementById("list_data").setAttribute('style', 'display:none')
    }
    else if (select.value == 'group_p3') {
        init_list_data(true, true)
        report_oth.$data.group_podly_ternerprof = true
        report_oth.$data.group_st_ot = true
        p_list_cast(450)
        document.getElementById("list_data").setAttribute('style', 'display:none')
    }
    else if (select.value == 'group_p4') {
        init_list_data(false, true)
        p_list_lit(350)
        document.getElementById("list_data").setAttribute('style', 'display:none')
    }
    else if (select.value == 'group_p5') {
        init_list_data(true, true)
        let data = ['stay_in_mo_filt']
        set_checked_filters(data)
        document.getElementById("stay_in_mo_filt_block").querySelector("input").style = "width:-moz-available;text-align: center;"
        p_list_cast(250)
    }
    else if (select.value == 'group_p6') {
        init_list_data(true, true)
        let data = ['kod_op_filt']
        set_checked_filters(data)
        document.getElementById("kod_op_filt_block").querySelector("input").style = "width:-moz-available;text-align: center;"
        p_list_cast(250)
    }
    else if (select.value == 'group_p7') {
        init_list_data(true, true)
        p_list_cast(250)
    }
    else if (select.value == 'group_p8') {
        init_list_data(true, true)
        let data = ['dskz_filt']
        set_checked_filters(data)
        p_list_cast(250)
    }
    else if (select.value == 'group_p9') {
        init_list_data(true, true)
        p_list_cast(250)
    }
    else if (select.value == 'group_p10') {
        init_list_data(true, true)
        let data = ['rai_in_filt']
        set_checked_filters(data)
        document.getElementById("rai_in_filt_block").querySelector("input").style = "width:-moz-available;text-align: center;"
        p_list_cast(250)
    }
    else if (select.value == 'group_p11') {
        init_list_data(true, true)
        p_list_cast(250)
    }
    else if (select.value == 'group_p12') {
        init_list_data(true, true)
        report_oth.$data.group_goc_filt = true
        document.getElementById("v_otdel_filter").style = "display: block;height: 200px;overflow-y: auto"
        p_list_cast(400)
    }
    else if (select.value == 'group_p13') {
        init_list_data(true, true)
        p_list_cast(250)
    }
    else if (select.value == 'group_p14') {
        init_list_data(true, true)
        p_list_cast(250)
    }

    else if (select.value == 'group_p15') {
        init_list_data(true, true)
        // let data = ['man_list','kod_vra_filt','otd_filt','fam_filt','age_group_filt','goc_filt','prpg_filt','pol_filt','dskz_filt','icx_filt']
        set_checked_filters(['man_list'])
        set_checked_filters(['kod_vra_filt'])
        set_checked_filters(['otd_filt'])
        set_checked_filters(['fam_filt'])
        set_checked_filters(['age_group_filt'])
        set_checked_filters(['goc_filt'])
        set_checked_filters(['prpg_filt'])
        set_checked_filters(['pol_filt'])
        set_checked_filters(['dskz_filt'])
        set_checked_filters(['icx_filt'])

        document.getElementById("man_list_block").querySelector("input").style = "width:-moz-available;text-align: center;"
        document.getElementById("kod_vra_filt_block").querySelector("input").style = "width:-moz-available;text-align: center;"
        document.getElementById("otd_filt_block").querySelector("input").style = "width:-moz-available;text-align: center;"
        document.getElementById("fam_filt_block").querySelector("input").style = "width:-moz-available;text-align: center;"
        document.getElementById("age_group_filt_block").querySelector("input").style = "width:-moz-available;text-align: center;"
        document.getElementById("goc_filt_block").querySelector("input").style = "width:-moz-available;text-align: center;"
        document.getElementById("prpg_filt_block").querySelector("input").style = "width:-moz-available;text-align: center;"
        document.getElementById("pol_filt_block").querySelector("input").style = "width:-moz-available;text-align: center;"
        // document.getElementById("dskz_filt_block").querySelector("input").style="width:-moz-available;text-align: center;"
        document.getElementById("icx_filt_block").querySelector("input").style = "width:-moz-available;text-align: center;"


        p_list_cast(400)
    }
    else if (select.value == 'group_p16') {
        init_list_data(true, true)
        let data = ['stay_in_mo_filt']
        set_checked_filters(data)
        document.getElementById("stay_in_mo_filt_block").querySelector("input").style = "width:-moz-available;text-align: center;"
        p_list_cast(250)
    }
    else if (select.value == 'group_p17') {
        init_list_data(true, true)
        p_list_cast(250)
    }
    else if (select.value == 'group_p18') {
        init_list_data(true, true)
        p_list_cast(250)
    }
    else if (select.value == 'group_p19') {
        init_list_data(true, true)
        p_list_cast(250)
    }
    else if (select.value == 'group_p20') {
        init_list_data(true, true)
        p_list_cast(250)
    }
    else if (select.value == 'group_p21') {
        init_list_data(true, true)
        p_list_cast(250)
    }
    else if (select.value == 'group_p22') {
        init_list_data(true, true)
        set_checked_filters(['otd_filt'])
        set_checked_filters(['metod_hmp'])
        set_checked_filters(['vid_hmp'])
        p_list_cast(350)

        document.getElementById("otd_filt_block").querySelector("input").style = "width:-moz-available;text-align: center;"
        document.getElementById("metod_hmp_block").querySelector("input").style = "width:-moz-available;text-align: center;"
        document.getElementById("vid_hmp_block").querySelector("input").style = "width:-moz-available;text-align: center;"
    }
    else if (select.value == 'group_p23') {
        init_list_data(true, true)
        p_list_cast(250)
    }
    else if (select.value == 'group_p24') {
        init_list_data(true, true)
        set_checked_filters(['dskz_filt'])
        set_checked_filters(['terr_filt'])

        document.getElementById("terr_filt_block").querySelector("input").style = "width:-moz-available;text-align: center;"

        p_list_cast(250)
    }
    else if (select.value == 'group_p25') {
        init_list_data(true, true)
        p_list_cast(250)
    }

}

function onchange_panel_init() {
    document.getElementById("panel-13-menu").value = ''
    document.getElementById("panel-14-menu").value = ''
    document.getElementById("panel-30-menu").value = ''
    document.getElementById("panel-16-menu").value = ''
    document.getElementById("panel-57-menu").value = ''
    document.getElementById("panel-pr-menu").value = ''
    document.getElementById("statistics_rep_btn").removeAttribute('btn')
}



function onchange_panel_13_menu(event) {
    let val = event.target.value
    onchange_panel_init()
    setTimeout(() => {
        document.getElementById("panel-13-menu").value = val
        document.getElementById("statistics_rep_btn").setAttribute('btn', val)
    }, 200)
}
function onchange_panel_14_menu(event) {
    let val = event.target.value
    onchange_panel_init()
    setTimeout(() => {
        document.getElementById("panel-14-menu").value = val
        document.getElementById("statistics_rep_btn").setAttribute('btn', val)
    }, 200)
}
function onchange_panel_30_menu(event) {
    let val = event.target.value
    onchange_panel_init()
    setTimeout(() => {
        document.getElementById("panel-30-menu").value = val
        document.getElementById("statistics_rep_btn").setAttribute('btn', val)
    }, 200)
}
function onchange_panel_16_menu(event) {
    let val = event.target.value
    onchange_panel_init()
    setTimeout(() => {
        document.getElementById("panel-16-menu").value = val
        document.getElementById("statistics_rep_btn").setAttribute('btn', val)
    }, 200)
}
function onchange_panel_57_menu(event) {
    let val = event.target.value
    onchange_panel_init()
    setTimeout(() => {
        document.getElementById("panel-57-menu").value = val
        document.getElementById("statistics_rep_btn").setAttribute('btn', val)
    }, 200)
}
function onchange_panel_pr_menu(event) {
    let val = event.target.value
    onchange_panel_init()
    setTimeout(() => {
        document.getElementById("panel-pr-menu").value = val
        document.getElementById("statistics_rep_btn").setAttribute('btn', val)
    }, 200)
}




function set_checked(data) {
    if (data.length > 0) {
        let list_input = document.getElementById("list_data").querySelectorAll("input")
        for (i of list_input) {
            if (data.indexOf(i.id) != -1) {
                i.checked = true
            }
        }
    }
}

function set_checked_filters(data) {
    if (data.length > 0) {
        let list_input = document.getElementById("filters_ul").querySelectorAll("input")
        for (i of list_input) {
            if (data.indexOf(i.id) != -1) {
                i.click()
            }
        }
    }
}

function on_checked_filter() {
    let list_input = document.getElementById("filters_ul").querySelectorAll("input")
    for (i of list_input) {
        if (i.checked) {
            i.click()
        }
    }
}
function get_otdel_filter() {
    let data = []
    let otd = document.getElementById("v_otdel_filter").querySelectorAll("input")
    for (i of otd) {
        if (i.checked) {
            data.push(i.value)
        }
    }
    return data
}

function onchange_group_st_ot(event) {

    report_oth.$data.group_shaping = false
    report_oth.$data.group_create = false
    report_oth.$data.group_error = false
    $("#group_download").empty()


    if (event.target.value == 'st') {
        report_oth.$data.v_otdel_filter = false
        document.getElementById("v_otdel_filter").style = "display: none"
    }
    else if (event.target.value == 'ot') {
        report_oth.$data.v_otdel_filter = true
        p_list_lit(450)
        document.getElementById("v_otdel_filter").style = "display: block;height: 200px;overflow-y: auto"

    }
}

function onchange_group_podly_ternerprof(event) {
    if (event.target.value == 'podly') {
        report_oth.$data.group_st_ot = true
    }
    else if (event.target.value == 'ternerprof') {
        report_oth.$data.group_st_ot = false
    }
}


