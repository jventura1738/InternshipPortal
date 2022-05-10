<template>
  <section
    class="text-gray-600 body-font relative flex h-screen justify-center items-center"
  >
    <div class="container px-5 py-24 mx-auto">
      <div class="flex flex-col text-center w-full mb-12">
        <h1
          class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900"
        >
          Contact Us
        </h1>
        <p class="lg:w-2/3 mx-auto leading-relaxed text-base">
          Leave any feedback or concerns you have below
        </p>
      </div>
      <div class="lg:w-1/2 md:w-2/3 mx-auto">
        <div class="flex flex-wrap -m-2">
          <div class="p-2 w-1/2">
            <div class="relative">
              <label for="name" class="leading-7 text-sm text-gray-600"
                >Name</label
              >
              <input
                type="text"
                id="name"
                name="name"
                v-model="name"
                class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
              />
            </div>
          </div>
          <div class="p-2 w-1/2">
            <div class="relative">
              <label for="email" class="leading-7 text-sm text-gray-600"
                >Email</label
              >
              <input
                type="email"
                id="email"
                name="email"
                v-model="email"
                class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
              />
            </div>
          </div>
          <div class="p-2 w-full">
            <div class="relative">
              <label for="message" class="leading-7 text-sm text-gray-600"
                >Message</label
              >
              <textarea
                id="message"
                name="message"
                v-model="message"
                class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"
              />
            </div>
          </div>
          <div class="p-2 w-full">
            <button
              class="flex mx-auto text-white border-0 py-2 px-8 focus:outline-none rounded text-lg"
              type="button"
              style="background-color: #8a0000"
              @click="submitForm"
            >
              Submit
            </button>
            <Modal
              v-if="show_modal"
              :ModalTitleProp="modal_title"
              :ModalMessageProp="modal_message"
            />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref } from "vue";
import Modal from "./Modal.vue";
export default {
  name: "ContactForm",
  components: {
    Modal,
  },
  setup() {
    const name = ref("");
    const email = ref("");
    const message = ref("");
    const show_modal = ref(false);
    const modal_title = ref("");
    const modal_message = ref("");

    const validateEmail = (email) => {
      return email.match(
        /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      );
    };

    async function submitForm() {
      const toSend = {
        name: name.value,
        email: email.value,
        message: message.value,
      };

      if (validateEmail(email.value)) {
        await fetch(`${process.env.SERVER_URL}/contact-submit`, {
          method: "POST",
          mode: "cors",
          credentials: "same-origin",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(toSend),
        }).then((res) => {
          if (res.status === 200) {
            name.value = "";
            email.value = "";
            message.value = "";
            show_modal.value = true;
            modal_title.value = "Submit Successful!";
            modal_message.value = "You successfully submitted the message.";
            setTimeout(() => {
              show_modal.value = false;
            }, 3000);
          } else {
            show_modal.value = true;
            modal_title.value = "Error!";
            modal_message.value =
              "An error occurred  while submitting. Please try again.";
            setTimeout(() => {
              show_modal.value = false;
            }, 3000);
          }
        });
      } else {
        show_modal.value = true;
        modal_title.value = "Error";
        modal_message.value = "Email provided is not valid. Please try again";
        setTimeout(() => {
          show_modal.value = false;
        }, 3000);
      }
    }
    return {
      name,
      email,
      message,
      show_modal,
      modal_title,
      modal_message,
      submitForm,
    };
  },
};
</script>
