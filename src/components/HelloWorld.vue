
<template>

  <v-container fluid>
    <!--<b-button size="sm" variant="primary" @click="close()">Close</b-button>
  -->
    <div>
      <v-alert v-if="type === 'info'" dense type="info">

      </v-alert>
      <v-alert v-if="type === 'success'" dense text type="success">
        BIENVENIDO
      </v-alert>
      <v-alert dense v-if="type === 'warning'" border="left" type="warning">
        Nombre de usurio o contraseña incorrectos
      </v-alert>
      <v-alert dense v-if="type === 'error'" outlined type="error">
        I'm a dense alert with the <strong>outlined</strong> prop and a <strong>type</strong> of error
      </v-alert>
    </div>

    <v-progress-linear color="teal" buffer-value="0" :value="getproceso()" stream></v-progress-linear>
    <v-stepper v-model="e1" non-linear :alt-labels="true">
      <v-expansion-panels v-model="n_panel">
        <v-expansion-panel key="0">
          <v-expansion-panel-header>
            Numero {{ e1 }}
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-stepper-header class="ma-0 pa-0">
              <template class="ma-0 pa-0" v-for="n in steps">
                <v-stepper-step :key="`${n}-step`" @click="pasar(n)" class="ma-0 pa-0" :step="n" editable
                  :complete="paso[n] == true">
                  Pregunata {{ n }}
                </v-stepper-step>

              </template>
            </v-stepper-header>
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>

      <v-stepper-items ref="contenido">

        <template class="ma-0 pa-0" v-for="n in steps">

          <v-stepper-content :ref="`${n}-content`" :key="`${n}-content`" :step="n">
            <v-row justify="center" no-gutters>

              <v-btn @click="prevStep(n)" dark small absolute top left icon class="mt-5" color="primary">
                <v-icon dark>mdi-skip-previous</v-icon>
              </v-btn>
              <v-col align="center" ref="card" justify="center" cols="12">

                Pregunta {{ n }}<br>


              </v-col>

              <v-btn @click="nextStep(n)" dark small absolute top right icon class="mt-5" color="primary">
                <v-icon dark>mdi-skip-next</v-icon>
              </v-btn>

            </v-row>
            <v-row>
              <v-col align="center" ref="card" justify="center" cols="12">
                {{ pregunta[n - 1].preguntas }}
              </v-col>

            </v-row>
            <v-row>
              <v-col>
                <hr>
                <v-radio-group v-model="valor">
                  <v-radio @click="nextStep(n)" label="Muy en desacuerdo" value="5"></v-radio>
                  <v-radio @click="nextStep(n)" label="Moderadamente en desacuerdo" value="4"></v-radio>
                  <v-radio @click="nextStep(n)" label="Ni de acuerdo, ni en desacuerdo" value="3"></v-radio>
                  <v-radio @click="nextStep(n)" label="Moderadamente de acuerdo" value="2"></v-radio>
                  <v-radio @click="nextStep(n)" label="Muy de acuerdo" value="1"></v-radio>
                </v-radio-group>

              </v-col>

            </v-row>


          </v-stepper-content>
        </template>

      </v-stepper-items>
    </v-stepper>
    <v-dialog v-model="dialog" width="600">


      <v-card align="center" ref="card" justify="center">



        <v-img max-height="200" max-width="300" src="https://media.tenor.com/i6FpdydNzhAAAAAj/si-se-puede-yes.gif">
        </v-img>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false">
            Continuar
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>

</template>

<script>
import axios from 'axios'
const Cookies = require('js-cookie');
export default {
  data: () => ({
    dialog: false,
    type: 'success',
    pregunta: [],
    colores: ["#FE0000", "#FF6600", "#FE9900", "#FFCC00", "#DFDF00", "#66CB01", "#009900", "#00CCCD", "#0066CB", "#670099", "#990099", "#CD0099"],
    select_option: '',
    panelIndex: 0,
    options: {
      duration: 200,
      offset: 0,
      easing: 'easeOutQuad',
    },
    e1: 1,
    steps: 70,
    paso: new Array(71).fill(false),
    date: null,
    trip: {
      name: '',
      location: null,
      start: null,
      end: null,
    },
    locations: ['Australia', 'Barbados', 'Chile', 'Denmark', 'Ecuador', 'France'],
    n_panel: '',
    valor: '',
    respuestas: {},
  }),
  mounted() {
    console.log(this.$refs);
    if (localStorage.getItem('token') && localStorage.getItem('refresh-token')
      && localStorage.getItem('user')) {

      this.actualizarpregunta()
    }
    else {
      this.$router.push('/login')
    }
  },
  Update() {
    this.actualizarpregunta();
    console.log(this.$refs['panel']);
    var p = this.panelIndex + 1
    this.$vuetify.goTo(this.$refs['panel'][p], this.options)

  },
  methods: {
    async actualizarpregunta() {
      const path = process.env.API_URL + "/pregunta/"
      var a = await axios({
        method: "get",
        url: path,
        data: '',
        headers: {
          'Content-Type': 'application/json',
          "X-CSRFToken": Cookies.get('csrftoken')
        },

      }).then((response) => {
        console.log(response.data)
        if (response.status == 200) {
          console.log("..", response)
          this.pregunta = response.data
        }
      })
        .catch((error) => {
          console.log(error);
        })
    },
    close() {
      const path = process.env.API_URL + "/logout/"
      console.log(path)
      //this.user.token=null
      console.log(JSON.parse(localStorage.getItem('user')))
      var datos = {
        token: localStorage.getItem('token'),
        name: JSON.parse(localStorage.getItem('user')).username,
        nuevo: '',
      }
      axios({
        method: "post",
        url: path,
        data: datos,
        headers: {
          'Content-Type': 'application/json',
          "X-CSRFToken": Cookies.get('csrftoken')
        },

      }).then((response) => {
        console.log(response.data)
        if (response.status == 200) {
          console.log(response)
          localStorage.clear()
          localStorage.removeItem('token-user')
          localStorage.removeItem('data-user')
          alert('se cerrado session')

          this.$router.push('/login')

        }
      })
        .catch((error) => {
          console.log(error);
        })
    },
    seleccion(i, p) {
      console.log("pregunta" + p, 'selecion' + i)
      this.select_option = i
      this.panelIndex += 1
      var panel = 'panel' + i;
      this.$vuetify.goTo(this.$refs['panel'][p], this.options)

    },
    nextStep(n) {
      console.log(this.getproceso())
      if (this.getproceso() >= 100) {
        alert(" finalizado el quiz")
        this.$router.push('/chatbot')
        return;
      }
      if (this.getproceso() == 30) {
        //alert(" finalizado el quiz")
        //this.$router.push('/chatbot')
        this.dialog = true
      }
      if (this.valor > 0) {
        this.respuestas[n] = this.valor
        this.paso[n] = true
        this.valor = ""
      }
      console.log(this.respuestas);
      if (n === this.steps) {
        this.e1 = 1
      } else {

        this.e1 = n + 1

      }
    },
    prevStep(n) {


      console.log(n)
      if (n - 1 <= 0) {
        n = this.e1 - 1
        return
      }

      if (n === this.steps) {
        this.e1 = 1
      } else {
        //this.paso[n] = true
        this.e1 = n - 1

      }
    },
    pasar(n) {
      console.log(this.$refs[n + '-content'])
      this.n_panel = ''
      this.$vuetify.goTo(this.$refs['contenido'], this.options)
    },
    getproceso() {
      //console.log(this.respuestas.length)
      console.log(Object.keys(this.respuestas).length)
      return parseInt((parseInt(Object.keys(this.respuestas).length) * 100) / parseInt(this.steps))
    }
  },

  created() {
    setTimeout(() => {
      this.type = ''
    }, 4000)
  },


}
</script>
