webpackJsonp([1],{"7zck":function(e,t){},"9M+g":function(e,t){},Jmt5:function(e,t){},NHnr:function(e,t,o){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var n=o("7+uW"),a={render:function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("v-app",[o("v-navigation-drawer",{attrs:{app:""},model:{value:e.drawer,callback:function(t){e.drawer=t},expression:"drawer"}}),e._v(" "),o("v-app-bar",{attrs:{app:""}},[o("v-app-bar-nav-icon",{on:{click:function(t){e.drawer=!e.drawer}}}),e._v(" "),o("v-toolbar-title",[e._v("Chatbot")])],1),e._v(" "),o("v-main",[o("router-view")],1)],1)},staticRenderFns:[]},r=o("VU/8")({name:"App",data:function(){return{drawer:null}}},a,!1,null,null,null).exports,s=o("/ocq"),i=o("fZjL"),l=o.n(i),c=o("Xxa5"),u=o.n(c),d=o("exGp"),p=o.n(d),v=o("mtWM"),f=o.n(v),m=o("ZQ6q"),g={data:function(){return{dialog:!1,type:"success",pregunta:[],colores:["#FE0000","#FF6600","#FE9900","#FFCC00","#DFDF00","#66CB01","#009900","#00CCCD","#0066CB","#670099","#990099","#CD0099"],select_option:"",panelIndex:0,options:{duration:200,offset:0,easing:"easeOutQuad"},e1:1,steps:70,paso:new Array(71).fill(!1),date:null,trip:{name:"",location:null,start:null,end:null},locations:["Australia","Barbados","Chile","Denmark","Ecuador","France"],n_panel:"",valor:"",respuestas:{}}},mounted:function(){console.log(this.$refs),localStorage.getItem("token")&&localStorage.getItem("refresh-token")&&localStorage.getItem("user")?this.actualizarpregunta():this.$router.push("/login")},Update:function(){this.actualizarpregunta(),console.log(this.$refs.panel);var e=this.panelIndex+1;this.$vuetify.goTo(this.$refs.panel[e],this.options)},methods:{actualizarpregunta:function(){var e=this;return p()(u.a.mark(function t(){var o;return u.a.wrap(function(t){for(;;)switch(t.prev=t.next){case 0:return o="/pregunta/",t.next=3,f()({method:"get",url:o,data:"",headers:{"Content-Type":"application/json","X-CSRFToken":m.get("csrftoken")}}).then(function(t){console.log(t.data),200==t.status&&(console.log("..",t),e.pregunta=t.data)}).catch(function(e){console.log(e)});case 3:t.sent;case 4:case"end":return t.stop()}},t,e)}))()},close:function(){var e=this;console.log("/logout/"),console.log(JSON.parse(localStorage.getItem("user")));var t={token:localStorage.getItem("token"),name:JSON.parse(localStorage.getItem("user")).username,nuevo:""};f()({method:"post",url:"/logout/",data:t,headers:{"Content-Type":"application/json","X-CSRFToken":m.get("csrftoken")}}).then(function(t){console.log(t.data),200==t.status&&(console.log(t),localStorage.clear(),localStorage.removeItem("token-user"),localStorage.removeItem("data-user"),alert("se cerrado session"),e.$router.push("/login"))}).catch(function(e){console.log(e)})},seleccion:function(e,t){console.log("pregunta"+t,"selecion"+e),this.select_option=e,this.panelIndex+=1;this.$vuetify.goTo(this.$refs.panel[t],this.options)},nextStep:function(e){if(console.log(this.getproceso()),this.getproceso()>=100)return alert(" finalizado el quiz"),void this.$router.push("/chatbot");30==this.getproceso()&&(this.dialog=!0),this.valor>0&&(this.respuestas[e]=this.valor,this.paso[e]=!0,this.valor=""),console.log(this.respuestas),e===this.steps?this.e1=1:this.e1=e+1},prevStep:function(e){console.log(e),e-1<=0?e=this.e1-1:e===this.steps?this.e1=1:this.e1=e-1},pasar:function(e){console.log(this.$refs[e+"-content"]),this.n_panel="",this.$vuetify.goTo(this.$refs.contenido,this.options)},getproceso:function(){return console.log(l()(this.respuestas).length),parseInt(100*parseInt(l()(this.respuestas).length)/parseInt(this.steps))}},created:function(){var e=this;setTimeout(function(){e.type=""},4e3)}},h={render:function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("v-container",{attrs:{fluid:""}},[o("div",["info"===e.type?o("v-alert",{attrs:{dense:"",type:"info"}}):e._e(),e._v(" "),"success"===e.type?o("v-alert",{attrs:{dense:"",text:"",type:"success"}},[e._v("\n      BIENVENIDO\n    ")]):e._e(),e._v(" "),"warning"===e.type?o("v-alert",{attrs:{dense:"",border:"left",type:"warning"}},[e._v("\n      Nombre de usurio o contraseña incorrectos\n    ")]):e._e(),e._v(" "),"error"===e.type?o("v-alert",{attrs:{dense:"",outlined:"",type:"error"}},[e._v("\n      I'm a dense alert with the "),o("strong",[e._v("outlined")]),e._v(" prop and a "),o("strong",[e._v("type")]),e._v(" of error\n    ")]):e._e()],1),e._v(" "),o("v-progress-linear",{attrs:{color:"teal","buffer-value":"0",value:e.getproceso(),stream:""}}),e._v(" "),o("v-stepper",{attrs:{"non-linear":"","alt-labels":!0},model:{value:e.e1,callback:function(t){e.e1=t},expression:"e1"}},[o("v-expansion-panels",{model:{value:e.n_panel,callback:function(t){e.n_panel=t},expression:"n_panel"}},[o("v-expansion-panel",{key:"0"},[o("v-expansion-panel-header",[e._v("\n          Numero "+e._s(e.e1)+"\n        ")]),e._v(" "),o("v-expansion-panel-content",[o("v-stepper-header",{staticClass:"ma-0 pa-0"},[e._l(e.steps,function(t){return[o("v-stepper-step",{key:t+"-step",staticClass:"ma-0 pa-0",attrs:{step:t,editable:"",complete:1==e.paso[t]},on:{click:function(o){return e.pasar(t)}}},[e._v("\n                Pregunata "+e._s(t)+"\n              ")])]})],2)],1)],1)],1),e._v(" "),o("v-stepper-items",{ref:"contenido"},[e._l(e.steps,function(t){return[o("v-stepper-content",{key:t+"-content",ref:t+"-content",refInFor:!0,attrs:{step:t}},[o("v-row",{attrs:{justify:"center","no-gutters":""}},[o("v-btn",{staticClass:"mt-5",attrs:{dark:"",small:"",absolute:"",top:"",left:"",icon:"",color:"primary"},on:{click:function(o){return e.prevStep(t)}}},[o("v-icon",{attrs:{dark:""}},[e._v("mdi-skip-previous")])],1),e._v(" "),o("v-col",{ref:"card",refInFor:!0,attrs:{align:"center",justify:"center",cols:"12"}},[e._v("\n\n              Pregunta "+e._s(t)),o("br")]),e._v(" "),o("v-btn",{staticClass:"mt-5",attrs:{dark:"",small:"",absolute:"",top:"",right:"",icon:"",color:"primary"},on:{click:function(o){return e.nextStep(t)}}},[o("v-icon",{attrs:{dark:""}},[e._v("mdi-skip-next")])],1)],1),e._v(" "),o("v-row",[o("v-col",{ref:"card",refInFor:!0,attrs:{align:"center",justify:"center",cols:"12"}},[e._v("\n              "+e._s(e.pregunta[t-1].preguntas)+"\n            ")])],1),e._v(" "),o("v-row",[o("v-col",[o("hr"),e._v(" "),o("v-radio-group",{model:{value:e.valor,callback:function(t){e.valor=t},expression:"valor"}},[o("v-radio",{attrs:{label:"Muy en desacuerdo",value:"5"},on:{click:function(o){return e.nextStep(t)}}}),e._v(" "),o("v-radio",{attrs:{label:"Moderadamente en desacuerdo",value:"4"},on:{click:function(o){return e.nextStep(t)}}}),e._v(" "),o("v-radio",{attrs:{label:"Ni de acuerdo, ni en desacuerdo",value:"3"},on:{click:function(o){return e.nextStep(t)}}}),e._v(" "),o("v-radio",{attrs:{label:"Moderadamente de acuerdo",value:"2"},on:{click:function(o){return e.nextStep(t)}}}),e._v(" "),o("v-radio",{attrs:{label:"Muy de acuerdo",value:"1"},on:{click:function(o){return e.nextStep(t)}}})],1)],1)],1)],1)]})],2)],1),e._v(" "),o("v-dialog",{attrs:{width:"600"},model:{value:e.dialog,callback:function(t){e.dialog=t},expression:"dialog"}},[o("v-card",{ref:"card",attrs:{align:"center",justify:"center"}},[o("v-img",{attrs:{"max-height":"200","max-width":"300",src:"https://media.tenor.com/i6FpdydNzhAAAAAj/si-se-puede-yes.gif"}}),e._v(" "),o("v-card-actions",[o("v-spacer"),e._v(" "),o("v-btn",{attrs:{color:"primary",text:""},on:{click:function(t){e.dialog=!1}}},[e._v("\n          Continuar\n        ")])],1)],1)],1)],1)},staticRenderFns:[]},_=o("VU/8")(g,h,!1,null,null,null).exports,k=o("ZQ6q"),b={data:function(){return{fields:[{key:"titulo",label:"Titulo"},{key:"nombre",label:"Nombre"},{key:"action",label:"Acccion"}],books:[],dato:""}},methods:{getBooks:function(){var e=this;f.a.get("/api/v1.0/books/").then(function(t){e.books=t.data}).catch(function(e){console.log(e)})},editar:function(e){console.log(e)},adicionar:function(){f.a.post("/adicionar/",{name:"name",date:"date"}).then(function(e){console.log(e.data)})},close:function(){var e=this;console.log("/logout/"),console.log(JSON.parse(localStorage.getItem("user")));var t={token:localStorage.getItem("token"),name:JSON.parse(localStorage.getItem("user")).username,nuevo:""};f()({method:"post",url:"/logout/",data:t,headers:{"Content-Type":"application/json","X-CSRFToken":k.get("csrftoken")}}).then(function(t){console.log(t.data),200==t.status&&(console.log(t),localStorage.clear(),localStorage.removeItem("token-user"),localStorage.removeItem("data-user"),alert("se cerrado session"),e.$router.push("/"))}).catch(function(e){console.log(e)})}},created:function(){this.getBooks()}},y={render:function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",{staticClass:"container"},[o("div",{staticClass:"row"},[o("div",{staticClass:"col text-left"},[o("h2",[e._v(" Listado Libros 2")]),e._v(" "),o("b-button",{attrs:{size:"sm",variant:"primary"},on:{click:function(t){return e.close()}}},[e._v("Close")]),e._v(" "),o("b-button",{attrs:{size:"sm",variant:"primary"},on:{click:function(t){return e.adicionar()}}},[e._v("Add")]),e._v(" "),o("div",{staticClass:"col-md-12"},[o("b-table",{attrs:{striped:"",hover:"",items:e.books,fields:e.fields},scopedSlots:e._u([{key:"cell(action)",fn:function(t){return[o("b-button",{attrs:{size:"sm",variant:"primary"},on:{click:function(o){return e.editar(t)}}},[e._v("Editar")]),e._v(" "),o("b-button",{attrs:{size:"sm",variant:"danger"},on:{click:function(o){return e.editar(t)}}},[e._v("Eliminar")])]}}])})],1)],1)])])},staticRenderFns:[]},x=o("VU/8")(b,y,!1,null,null,null).exports,w=o("mvHQ"),S=o.n(w),C=o("ZQ6q"),I={name:"HelloWorld",components:{App:r},data:function(){return{type:"",dialog:!0,tab:0,tabs:[{name:"Inicio de Sesion",icon:"mdi-account"},{name:"Registro",icon:"mdi-account-outline"}],valid:!0,user:{},error:{},loginEmailRules:[function(e){return!!e||"Se requiere completar"}],emailRules:[function(e){return!!e||"Se requiere completar"}],show1:!1,rules:{required:function(e){return!!e||"Se requiere completar"},min:function(e){return e&&e.length>=4||"Minimo 4 Caracteres"}},verify:null,activePicker:null,date:null,menu:!1}},mounted:function(){localStorage.getItem("token")&&localStorage.getItem("refresh-token")&&localStorage.getItem("user")&&this.$router.push("/inicio")},watch:{menu:function(e){var t=this;e&&setTimeout(function(){return t.activePicker="YEAR"})}},computed:{passwordConfirmationRule:function(){var e=this;return function(){return e.verify===e.user.password||"Contraseña no coincide"}}},methods:{validate:function(){var e=this;if(this.$refs.loginForm.validate()){console.log("/login/"),f()({method:"post",url:"/login/",data:this.user,headers:{"Content-Type":"application/json","X-CSRFToken":C.get("csrftoken")}}).then(function(t){console.log(t.data),200==t.status&&(e.type="success",localStorage.setItem("token",t.data.token),localStorage.setItem("refresh-token",t.data["refresh-token"]),localStorage.setItem("user",S()(t.data.user)),e.$router.push("/inicio"))}).catch(function(t){e.type="warning",console.log(t)})}},save:function(e){this.$refs.menu.save(e)},register:function(){var e=this;if(this.$refs.registerForm.validate()){f()({method:"post",url:"/users/",data:this.user,headers:{"Content-Type":"application/json","X-CSRFToken":C.get("csrftoken")}}).then(function(t){if(console.log(t.data),200==t.status)return e.type="success",localStorage.setItem("token",t.data.token),localStorage.setItem("refresh-token",t.data["refresh-token"]),localStorage.setItem("user",S()(t.data.user)),void e.$router.push("/inicio");400==t.status&&console.log(t.data)}).catch(function(t){e.type="warning",console.log(t.response.data.errors),e.error=t.response.data.errors,e.valid=!0})}return!1}}},$={render:function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("v-container",{attrs:{fluid:""}},[o("div",["info"===e.type?o("v-alert",{attrs:{dense:"",type:"info"}},[e._v("\n            I'm a dense alert with a "),o("strong",[e._v("type")]),e._v(" of info\n        ")]):e._e(),e._v(" "),"success"===e.type?o("v-alert",{attrs:{dense:"",text:"",type:"success"}},[e._v("\n            Welcome\n        ")]):e._e(),e._v(" "),"warning"===e.type?o("v-alert",{attrs:{dense:"",border:"left",type:"warning"}},[e._v("\n            Nombre de usurio o contraseña incorrectos\n        ")]):e._e(),e._v(" "),"error"===e.type?o("v-alert",{attrs:{dense:"",outlined:"",type:"error"}},[e._v("\n            I'm a dense alert with the "),o("strong",[e._v("outlined")]),e._v(" prop and a "),o("strong",[e._v("type")]),e._v(" of error\n        ")]):e._e()],1),e._v(" "),o("v-tabs",{attrs:{"show-arrows":"","background-color":"deep-purple accent-4","icons-and-text":"",dark:"",grow:""},model:{value:e.tab,callback:function(t){e.tab=t},expression:"tab"}},[o("v-tabs-slider",{attrs:{color:"purple darken-4"}}),e._v(" "),e._l(e.tabs,function(t,n){return o("v-tab",{key:n},[o("v-icon",{attrs:{large:""}},[e._v(e._s(t.icon))]),e._v(" "),o("div",{staticClass:"caption py-1"},[e._v(e._s(t.name))])],1)}),e._v(" "),o("v-tab-item",[o("v-card",{staticClass:"px-4"},[o("v-card-text",[o("v-form",{ref:"loginForm",attrs:{"lazy-validation":""},on:{action:e.validate}},[o("v-row",[o("v-col",{attrs:{cols:"12"}},[o("v-text-field",{attrs:{rules:e.loginEmailRules,label:"Nombre de Usuario",required:""},model:{value:e.user.username,callback:function(t){e.$set(e.user,"username",t)},expression:"user.username"}})],1),e._v(" "),o("v-col",{attrs:{cols:"12"}},[o("v-text-field",{attrs:{"append-icon":e.show1?"eye":"eye-off",rules:[e.rules.required,e.rules.min],type:e.show1?"text":"password",name:"input-10-1",label:"Constaseña",hint:"Minimo 8 caracteres",counter:""},on:{"click:append":function(t){e.show1=!e.show1}},model:{value:e.user.password,callback:function(t){e.$set(e.user,"password",t)},expression:"user.password"}})],1),e._v(" "),o("v-col",{staticClass:"d-flex",attrs:{cols:"12",sm:"6",xsm:"12"}}),e._v(" "),o("v-spacer"),e._v(" "),o("v-col",{staticClass:"d-flex",attrs:{cols:"12",sm:"3",xsm:"12","align-end":""}},[o("v-btn",{attrs:{"x-large":"",block:"",disabled:!e.valid,color:"success"},on:{click:e.validate}},[e._v(" Iniciar\n                                    Sesion ")])],1)],1)],1)],1)],1)],1),e._v(" "),o("v-tab-item",[o("v-card",{staticClass:"px-4"},[o("v-card-text",[o("v-form",{ref:"registerForm",attrs:{"lazy-validation":""}},[o("v-row",[o("v-col",{attrs:{cols:"12"}},[o("v-text-field",{attrs:{rules:[e.rules.required],label:"Nick","error-messages":e.error.username,maxlength:"20",required:""},model:{value:e.user.username,callback:function(t){e.$set(e.user,"username",t)},expression:"user.username"}})],1),e._v(" "),o("v-col",{attrs:{cols:"12"}},[o("v-text-field",{attrs:{label:"Nombre Completo",maxlength:"20"},model:{value:e.user.name,callback:function(t){e.$set(e.user,"name",t)},expression:"user.name"}})],1),e._v(" "),o("v-col",{attrs:{cols:"12"}},[o("v-menu",{ref:"menu",attrs:{"close-on-content-click":!1,transition:"scale-transition","offset-y":"","min-width":"auto"},scopedSlots:e._u([{key:"activator",fn:function(t){var n=t.on,a=t.attrs;return[o("v-text-field",e._g(e._b({attrs:{rules:[e.rules.required],label:"Fecha de Nacimineto","prepend-icon":"mdi-calendar",readonly:""},model:{value:e.user.bith_date,callback:function(t){e.$set(e.user,"bith_date",t)},expression:"user.bith_date"}},"v-text-field",a,!1),n))]}}]),model:{value:e.menu,callback:function(t){e.menu=t},expression:"menu"}},[e._v(" "),o("v-date-picker",{attrs:{"active-picker":e.activePicker,locale:"es-ES",max:new Date(Date.now()-6e4*(new Date).getTimezoneOffset()).toISOString().substr(0,10),min:"1950-01-01"},on:{"update:activePicker":function(t){e.activePicker=t},"update:active-picker":function(t){e.activePicker=t},change:function(t){return e.save(e.user.bith_date)}},model:{value:e.user.bith_date,callback:function(t){e.$set(e.user,"bith_date",t)},expression:"user.bith_date"}})],1)],1),e._v(" "),o("v-col",{attrs:{cols:"12"}},[o("v-text-field",{attrs:{"error-messages":e.error.email,label:"E-mail"},model:{value:e.user.email,callback:function(t){e.$set(e.user,"email",t)},expression:"user.email"}})],1),e._v(" "),o("v-col",{attrs:{cols:"12"}},[o("v-text-field",{attrs:{"append-icon":e.show1?"mdi-eye":"mdi-eye-off",rules:[e.rules.required,e.rules.min],type:e.show1?"text":"password",name:"input-10-1",label:"Password",hint:"At least 8 characters",counter:""},on:{"click:append":function(t){e.show1=!e.show1}},model:{value:e.user.password,callback:function(t){e.$set(e.user,"password",t)},expression:"user.password"}})],1),e._v(" "),o("v-col",{attrs:{cols:"12"}},[o("v-text-field",{attrs:{block:"","append-icon":e.show1?"mdi-eye":"mdi-eye-off",rules:[e.rules.required,e.passwordConfirmationRule],type:e.show1?"text":"password",name:"input-10-1",label:"Confirm Password",counter:""},on:{"click:append":function(t){e.show1=!e.show1}},model:{value:e.verify,callback:function(t){e.verify=t},expression:"verify"}})],1),e._v(" "),o("v-spacer"),e._v(" "),o("v-col",{staticClass:"d-flex ml-auto",attrs:{cols:"12",sm:"3",xsm:"12"}},[o("v-btn",{attrs:{"x-large":"",block:"",disabled:!e.valid,color:"success"},on:{click:e.register}},[e._v("Registro\n                                ")])],1)],1)],1)],1)],1)],1)],2)],1)},staticRenderFns:[]},F=o("VU/8")(I,$,!1,null,null,null).exports;n.default.use(s.a);var T=new s.a({routes:[{path:"/",name:"HelloWorld",component:_},{path:"/books",name:"ListBook",component:x},{path:"/inicio",name:"Inicio",component:_},{path:"/login",name:"Login",component:F}],mode:"history"}),q=o("Tqaz"),N=(o("Jmt5"),o("9M+g"),o("gJtD"),o("csSS"),o("3EgV")),E=o.n(N),R=(o("7zck"),o("ppUw")),z=o.n(R),A=o("ZQ6q");n.default.config.productionTip=!1,n.default.use(A),n.default.use(z.a),n.default.use(q.a),n.default.use(q.b),n.default.use(E.a);t.default=new E.a({icons:{iconfont:"mdi"}});new n.default({el:"#app",router:T,vuetify:new E.a,components:{App:r},template:"<App/>"})},csSS:function(e,t){},gJtD:function(e,t){}},["NHnr"]);
//# sourceMappingURL=app.07f4ca261bb5fb1579dc.js.map