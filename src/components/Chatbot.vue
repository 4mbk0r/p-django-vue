<template>
    <v-container class="fill-height pa-0 ">
        <v-row class="no-gutters elevation-4">
            <v-col cols="12" sm="3" class="flex-grow-1 flex-shrink-0" style="border-right: 1px solid #0000001f;">
                <v-responsive class="overflow-y-auto fill-height" max-height="600">
                    <v-list subheader>
                        <v-list-item-group v-model="activeChat">
                            <template v-for="(item, index) in parents">
                                <v-list-item :key="`parent${index}`" :value="item.id">
                                    <v-list-item-avatar color="grey lighten-1 white--text">
                                        <v-icon>
                                            chat_bubble
                                        </v-icon>
                                    </v-list-item-avatar>
                                    <v-list-item-content>
                                        <v-list-item-title v-text="item.title" />
                                        <v-list-item-subtitle v-text="'hi'" />
                                    </v-list-item-content>
                                    <v-list-item-icon>
                                        <v-icon :color="item.active ? 'deep-purple accent-4' : 'grey'">
                                            chat_bubble
                                        </v-icon>
                                    </v-list-item-icon>
                                </v-list-item>
                                <v-divider :key="`chatDivider${index}`" class="my-0" />
                            </template>
                        </v-list-item-group>
                    </v-list>
                </v-responsive>
            </v-col>
            <v-col cols="auto" class="flex-grow-1 flex-shrink-0">
                <v-responsive v-if="activeChat" class="overflow-y-hidden fill-height" max-height="600">
                    <v-card flat class="d-flex flex-column fill-height">
                        <v-card-title>
                            Chatbot
                        </v-card-title>
                        <v-card-text class="flex-grow-1 overflow-y-auto">
                            <template v-for="(msg, i) in messages">
                                <div :class="{ 'd-flex flex-row-reverse': msg.me }">
                                    <v-menu offset-y>
                                        <template v-slot:activator="{ on }">
                                            <v-hover v-slot:default="{ hover }">
                                                <v-chip :id="'chat-i'" :color="msg.me ? 'primary' : ''" dark
                                                    style="height:auto;white-space: normal;" class="pa-4 mb-2"
                                                    v-on="on">
                                                    {{ msg.content }}
                                                    <!--<sub class="ml-2" style="font-size: 0.5rem;">{{ msg.created_at
                                                    }}</sub>-->
                                                    <v-icon v-if="hover" small>
                                                        expand_more
                                                    </v-icon>
                                                </v-chip>
                                            </v-hover>
                                        </template>
                                        <v-list>
                                            <v-list-item>
                                                <v-list-item-title>Eliminar</v-list-item-title>
                                            </v-list-item>
                                        </v-list>
                                    </v-menu>
                                </div>
                            </template>
                        </v-card-text>
                        <v-card-text class="flex-shrink-1">
                            <v-text-field v-model="messageForm.content" label="Escribe tu respuesta" type="text"
                                no-details outlined append-outer-icon="send" @keyup.enter="send"
                                @click:append-outer="send" hide-details />
                        </v-card-text>
                    </v-card>
                </v-responsive>
            </v-col>
        </v-row>
    </v-container>

</template>

<script>
import axios from 'axios'

const Cookies = require('js-cookie');
export default {
    data: () => ({
        activeChat: 1,
        parents: [
            {
                id: 1,
                title: "Chatbot",
                active: true
            },

        ],
        nro: 0,
        preguntas: [
            {
                "content": "1.\t¿Qué actividades o actitudes consideras funcionales, sanas o constructivas dentro de una relación? Por ejemplo: negociar tiempos juntos y con amigos, expresar de forma sincera sobre cómo se sienten con una situación, comunicación constante y sincera, darse su espacio personal",
                "numero": "1",

                "created_at": ""
            },
            {
                "content": "2.\t¿Qué acciones son las que realizas para poder controlar, mitigar o gestionar una situación complicada o muy difícil con tu pareja? Por ejemplo: diálogo, negociación o poner orden para que cada uno tenga su tiempo.",
                "numero": "2",

                "created_at": ""
            },
            {
                "content": "3.\t¿Qué te motiva a intentar controlar o enfrentar sanamente una situación cuando hay problemas con tu pareja? Por ejemplo: la misma relación, el bienestar de ambos, el tiempo que llevan en pareja.",
                "numero": "3",

                "created_at": ""
            },
            {
                "content": "4.\t¿Qué haces cuando tienes una discusión con tu pareja para que dicha discusión no se salga de control y el resultado de esto sea positivo ambos y para su relación? Por ejemplo: darse unos minutos u horas para enfriar el ambiente, poner orden en el cual cada uno dará su opinión  u otro. ",
                "numero": "4",

                "created_at": ""
            },
            {
                "content": "5.\t¿Qué actitudes o acciones te han servido para expresarle a tu pareja saludablemente tus celos o reducirlos cuando los sientes? Por ejemplo: tener más atenciones con tu pareja, hacerle saber cuáles momentos fueron incómodos debido a los celos que sentías. ",
                "numero": "5",

                "created_at": ""
            },
            {
                "content": "6.\t¿Cómo sabes que lo que has hecho ha sido positivo para mejorar o mantener tu relación?",
                "numero": "6",

                "created_at": ""
            },
            {
                "content": "7.\t¿Qué podrías hacer para que la situación con tu pareja mejore?",
                "numero": "7",

                "created_at": ""
            },
            {
                "content": "8.\tImagina que una noche te vas a dormir y que ocurre un milagro, despiertas y el problema con tu pareja ya no existe, o por lo menos los principales problemas ya no existen. ¿Qué es lo primero que te indicaría que ha ocurrido el milagro?",
                "numero": "8",

                "created_at": ""
            },
            {
                "content": "9.\t¿Qué te ayudó a llegar hasta donde estás hoy en tu relación?",
                "numero": "9",

                "created_at": ""
            },
            {
                "content": "10.\t¿Qué está impidiendo que las cosas empeoren en tu relación ahora mismo dentro de tu relación?",
                "numero": "10",

                "created_at": ""
            },
            {
                "content": "11.\t¿Qué te indica que las cosas están mejorando o que no se están poniendo peores en tu relación?",
                "numero": "11",

                "created_at": ""
            },
            {
                "content": "12.\t¿Cómo has afrontado y salido triunfante de situaciones similares con tu pareja en el pasado? Por ejemplo: la vez que hablaste de manera sincera con tu pareja o cuando se dieron tiempos para poder hablar y expresarse. ",
                "numero": "12",

                "created_at": ""
            },
            {
                "content": "13.\t¿Qué actitudes o actividades realizarás para mantener tu relación saludable (es decir que la relación sea un punto de apoyo y no de dificultades) y con planes hacia el futuro? Por ejemplo: darle su espacio personal, expresar de manera sincera sobre cómo te sientes.",
                "numero": "13",

                "created_at": ""
            },
            {
                "content": "14.\t¿Cómo es tu relación cuando no está presente un problema fuerte o grave?",
                "numero": "14",

                "created_at": ""
            }
        ],
        messages: [],
        messageForm: {
            content: "",
            me: true,
            created_at: "11:11am"
        }
    }),
    methods: {
        send: function () {
            this.messages.push(structuredClone(this.messageForm))
            this.addfirst()

        },
        addReply() {
            this.chat.push({
                from: "sushant",
                msg: "Hmm"
            })
        },
        addfirst() {
            this.messages.push(this.preguntas[this.nro])
            this.nro += 1
            //document.getElementById("chat-" + this.messages.length - 1).scrollIntoView()
        }
    },
    created() {
        this.addfirst()
    }


}
</script>