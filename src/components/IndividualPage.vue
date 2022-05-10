<template>
  <div
    class="relative shadow-xl border-2 rounded-xl px-8 pt-6 pb-8 mb-4 flex flex-col my-2 mx-auto my-auto w-1/2 mt-12"
  >
    <div class="text-center mb-12 mt-4">
      <div class="text-3xl font-extrabold">{{ position }}</div>
    </div>
    <div class="text-justify mb-12">
      <div class="text-lg p-2">
        <span class="font-bold"> Minimum Qualifications: </span
        >
        <ul class="list-none">
          <li>{{ min_qualifications }}</li>
        </ul>
      </div>
      <div class="text-lg p-2">
        <span class="font-bold"> Preferred Qualifications: </span
        >
        
        <ul class="list-none">
          <li>{{ pref_qualifications }}</li>
        </ul>
      </div>
      <div class="text-lg p-2">
        <span class="font-bold"> Position Responsibilities: </span
        >
        
        <ul class="list-none">
          <li>{{ pos_responsibility }}</li>
        </ul>
      </div>
      <div v-if="additional_info">
        <div class="text-lg p-2">
          <span class="font-bold"> Additional Information: </span
          >
          
          <ul class="list-none">
            <li>{{ additional_info }}</li>
          </ul>
        </div>
      </div>
      <div class="text-lg p-2">
        <span class="font-bold"> Position Duration: </span
        >
        
        <ul class="list-none">
          <li>{{ duration }} weeks</li>
        </ul>
      </div>
      <div class="text-lg text-center font-bold p-2 pt-5">
        Application Dates  
      </div>
      <div class="text-lg text-center p-2">
        <span class="font-bold"> Open: </span>{{ app_open }}
        <span class="font-bold pl-3"> Close: </span>{{ app_close }}
      </div>
    </div>
    <div class="">
      <button class="absolute bottom-9 left-9 " @click="toBrowsePage">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="36"
            height="36"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
            class="feather feather-arrow-left"
          >
            <line x1="19" y1="12" x2="5" y2="12"></line>
            <polyline points="12 19 5 12 12 5"></polyline>
          </svg>
        </button>
    </div>
    <div v-if="app_link != null" class="mx-auto">
      <a :href="app_link" @click="incrementApplications">
        <button
          class="bg-primary hover:bg-primaryOffset text-white font-bold py-2 px-4 rounded w-full"
        >
          Apply
        </button>
      </a>
    </div>
    <div v-if="app_link == null" class="mx-auto">
      <button
        class="bg-gray-300 text-white font-bold py-2 px-4 rounded w-full cursor-not-allowed"
        disabled
      >
        No Application Link
      </button>
    </div>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";
export default {
  name: "IndividualPage",
  setup() {
    const listing = ref({});
    const id = ref("");
    const position = ref("");
    const min_qualifications = ref("");
    const pref_qualifications = ref("");
    const pos_responsibility = ref("");
    const additional_info = ref("");
    const duration = ref("");
    const app_open = ref("");
    const app_close = ref("");
    const app_link = ref("");
    onMounted(async () => {
      let uri = window.location.search.substring(1);
      let params = new URLSearchParams(uri);
      let lid = params.get("id");
      let result = await fetch(
        `${process.env.SERVER_URL}/get-listing/${lid}`
      ).catch((error) => {
        console.log(error);
      });
      let l = await result.json();
      console.log(l);
      id.value = l.listing.id;
      position.value = l.listing.position;
      min_qualifications.value = l.listing.min_qualifications;
      pref_qualifications.value = l.listing.pref_qualifications;
      pos_responsibility.value = l.listing.pos_responsibility;
      additional_info.value = l.listing.additional_info;
      duration.value = l.listing.duration;
      app_open.value = l.listing.app_open;
      app_close.value = l.listing.app_close;
      app_link.value = l.listing.app_link;
      console.log("link", l.listing.app_link);
    });

    async function incrementApplications() {
      const toSend = {
        statistic: "applications",
      };
      await fetch(`${process.env.SERVER_URL}/modify-statistics/${id.value}`, {
        method: "PUT",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(toSend),
      })
        .then((res) => {
          if (res.status === 200) {
            console.log("SUCCESS");
            window.location.href = `/listing?id=${listing_id}`;
          } else if (res.status === 404) {
            console.log("FAILED");
          } else {
            console.log("ERROR");
          }
        })
        .catch((err) => {
          console.log(err);
        });
    }

    function toBrowsePage() {
            window.location.href = "/browse";
    }
    
    return {
      id,
      position,
      min_qualifications,
      pref_qualifications,
      pos_responsibility,
      additional_info,
      duration,
      app_open,
      app_close,
      app_link,
      toBrowsePage,
      incrementApplications,
    };
  },
};
</script>
