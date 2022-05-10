<template>
  <div class="flex flex-wrap mx-auto my-auto">
    <div
      v-for="listing in listings"
      class="sm:flex-sm md:flex-md lg:flex-lg last:flex-el flex-nm m-4 shadow-xl rounded-xl bg-white cursor-pointer border-2 border-gray-200"
      :key="listing[1].listing.id"
      @click="toListingPage(listing[1].listing.id)"
    >
      <div class="px-6 py-4">
        <div class="relative">
          <div class="absolute top-2 left-0">
            <img src="../img/seagull.svg" height="30" width="30" />
          </div>
        </div>
        <div class="text-center text-gray-900 font-bold text-xl mb-2">
          {{ listing[1].listing.position }}
        </div>
        <p class="text-center text-gray-900 font-semibold text-base">
          <span class="text-gray-500 font-normal">{{ listing[1].client }}</span>
        </p>
        <div class="text-gray-900 font-semibold text-base">
          Tags:
          <div
            v-if="listing[1].tags != null && listing[1].tags.length > 0"
            class="mb-2"
          >
            <div v-for="tag in listing[1].tags" :key="tag">
              <span
                class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-200 text-gray-600"
              >
                {{ tag }}
              </span>
            </div>
          </div>
          <div v-else>
            <span
              class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-200 text-red-600"
            >
              No Tags
            </span>
          </div>
        </div>
        <div class="text-gray-900 font-semibold text-base">
          SU Courses:
          <div
            v-if="listing[1].courses != null && listing[1].courses.length > 0"
            class="mb-2"
          >
            <div v-for="course in listing[1].courses" :key="course">
              <span
                class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-gray-200 text-gray-600"
              >
                {{ course }}
              </span>
            </div>
          </div>
          <div v-else>
            <span
              class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-200 text-red-600"
            >
              No Courses
            </span>
          </div>
        </div>
        <div class="relative">
          <div
            class="absolute bottom-8 right-0 text-white font-semibold text-base"
          >
            <span
              class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-800"
            >
              Open: {{ listing[1].listing.app_open }}
            </span>
          </div>
          <div
            class="absolute bottom-2 right-0 text-white font-semibold text-base"
          >
            <span
              class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-red-800"
            >
              Close: {{ listing[1].listing.app_close }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BrowseListingCard",
  props: ["listings"],
  setup() {
    const toSend = {
      statistic: "views",
    };
    async function toListingPage(listing_id) {
      await fetch(`${process.env.SERVER_URL}/modify-statistics/${listing_id}`, {
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
    return {
      toListingPage,
    };
  },
};
</script>
