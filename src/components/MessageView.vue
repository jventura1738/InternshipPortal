<template>
    <section>
        <div class="pt-28 pb-20 px-10 mx-auto my-auto">
            <div class="container w-3/5 shadow-md bg-gray-100 mx-auto my-auto px-10 pt-10 pb-10 text-left rounded-lg">
           
        
                <div class="block uppercase font-bold text-gray-500">
                    <div class="block uppercase font-bold text-black">Name: </div>
                    <svg 
                  xmlns="http://www.w3.org/2000/svg" 
                  class="float-right cursor-pointer w-5 h-5 rounded-sm hover:bg-gray-400" 
                  @click="deleteMessage(id)"
                  viewBox="0 0 24 24">
                  <path d="M3 6v18h18v-18h-18zm5 14c0 
                  .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 
                  .448 1 1v10zm5 0c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 
                  .448 1 1v10zm5 0c0 .552-.448 1-1 1s-1-.448-1-1v-10c0-.552.448-1 1-1s1 .448 
                  1 1v10zm4-18v2h-20v-2h5.711c.9 0 1.631-1.099 1.631-2h5.315c0 .901.73 2 1.631 2h5.712z"/>
                  </svg>
                </div>

                    <h1 class="block font-large text-gray-700">
                            {{ name }}
                    </h1>
                
                <div class="block uppercase font-bold text-black">Email: </div>
                    <h2 class="block font-large text-gray-700 pb-8">
                            {{ email }}
                    </h2>
                
                <div class="block uppercase font-bold text-black pb-1">Message: 
                </div>
                    <div class="container bg-white mx-auto my-auto px-10 py-24 pt-10 pb-52 text-left rounded-lg">           
                    <p class="block font-large text-gray-700 text-left">
                            {{ message }}
                    </p>
                    </div>   
                
                <div class="pt-5">
                 <button class="inline-flex items-center block uppercase text-black font-bold bg-white border-0 py-1 px-3 focus:outline-none hover:bg-gray-100 rounded text-base mt-4 md:mt-0" @click="toInboxPage">Back</button>   
                </div>
            </div>

            <Modal
              v-if="show_modal"
              :ModalTitleProp="modal_title"
              :ModalMessageProp="modal_message"
            />
        </div>

    </section>
</template>

<script>
import { ref, onMounted } from "vue";
import Modal from "./Modal.vue";
export default {
    name: "MessageView",
    components: {
    Modal,
    },
    setup() {
        const id = ref(0); 
        const name = ref(""); 
        const email = ref(""); 
        const message = ref(""); 
        const show_modal = ref(false);
        const modal_title = ref("");
        const modal_message = ref("");
        

        onMounted(async () =>{
            let uri = window.location.search.substring(1);
            let params = new URLSearchParams(uri);
            let message_id = params.get("id");

            let result = await fetch(
            `${process.env.SERVER_URL}/admin/get-message/${message_id}`
            ).catch((error) => {
            console.log(error);
            });
            let messages = await result.json();
      
            let m = messages.message; 
            console.log(m); 
            id.value = m.id; 
            name.value = m.name; 
            email.value = m.email; 
            message.value = m.message; 
        });

        function deleteMessage(message_id){
            fetch(`${process.env.SERVER_URL}/admin/delete_message/${message_id}`, {
            method: "DELETE",
            mode: "cors",
            credentials: "same-origin",
            headers: {
            "Content-Type": "application/json",
            },
            }).then((res) => {
                if (res.status === 200) {
                    console.log("Message Successfully Deleted");
                    window.location.href = "/admin/contactinbox";
                } else {
                    show_modal.value = true;
                    modal_title.value = "Error!";
                    modal_message.value =
                    "An error occurred  while submitting. Please try again.";
                }
            });
        };
        
        function toInboxPage() {
            window.location.href = "/admin/contactinbox";
        };

        return {
            id, 
            name, 
            email, 
            message, 
            show_modal,
            modal_title,
            modal_message,
            toInboxPage,
            deleteMessage,
        };
    },
};
</script>
