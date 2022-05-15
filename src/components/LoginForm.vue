<template>
  <div class="bg-gray-100 flex h-screen justify-center items-center">
    <div
      class="bg-white lg:w-4/12 md:6/12 w-10/12 m-auto my-10 shadow-md rounded-xl"
    >
      <div class="py-6 px-8 rounded-xl">
        <h1 class="text-3xl font-sans font-extrabold text-center">
          Admin Login
        </h1>
        <form>
          <div class="my-5 text-sm">
            <label class="block text-black">Username</label>
            <input
              type="text"
              autofocus
              autocomplete="off"
              class="rounded-lg px-4 py-3 mt-3 focus:outline-none bg-gray-100 w-full"
              placeholder="Username"
              v-model="username"
            />
          </div>
          <div class="my-5 text-sm">
            <label for="password" class="block text-black">Password</label>
            <input
              type="password"
              autocomplete="off"
              class="px-4 py-3 mt-3 focus:outline-none bg-gray-100 w-full rounded-lg"
              placeholder="Password"
              v-model="password"
            />
          </div>
          <div class="flex items-center justify-between">
            <button
              class="block text-center text-white bg-primary p-3 duration-300 hover:bg-red-700 w-1/3 rounded-lg mb-3 mt-2"
              type="button"
              @click="submitForm"
            >
              Sign In
            </button>
            <input type="submit" @click="submitForm" style="display: none" />
            <a
              class="inline-block align-top underline font-bold text-sm text-blue hover:text-primary"
              href="/login/reset-password"
            >
              Forgot Password?
            </a>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
export default {
  name: "LoginForm",
  setup() {
    const username = ref("");
    const password = ref("");

    async function submitForm(event) {
      event.preventDefault();
      const username = this.username;
      const password = this.password;
      const toSend = { username, password };
      await fetch(`${process.env.SERVER_URL}/login-submit`, {
        method: "POST",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(toSend),
      })
        .then((res) => {
          if (res.status === 200) {
            window.location.href = "/admin";
          } else if (res.status === 403) {
            res.json().then((r) => {
              alert(r.err_msg);
            });
          }
        })
        .catch((err) => {
          console.log(err);
        });
    }

    return {
      username,
      password,
      submitForm,
    };
  },
};
</script>
