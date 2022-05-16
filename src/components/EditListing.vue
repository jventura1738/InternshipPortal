<template>
  <form class="flex justify-center items-center">
    <div class="px-8 pt-6 pb-8 mb-4 mt-6 my-2 m-auto w-full">
      <h1
        class="block uppercase tracking-wide text-grey-darker text-3xl font-bold mb-2 mt-2 text-center"
      >
        Editing Listing #{{ id }}
      </h1>
      <div class="-mx-3 flex flex-wrap mb-6">
        <div
          class="w-full px-3 flex-nm xs:flex-nm sm:flex-nm md:flex-nm lg:flex-nm xl:flex-el"
        >
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            >Position Title</label
          >
          <input
            class="outline-none appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6"
            required
            type="text"
            v-model="position"
          />
        </div>
        <div
          class="w-full px-3 flex-nm xs:flex-nm sm:flex-nm md:flex-nm lg:flex-nm xl:flex-el"
        >
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            >Position Responsibilities</label
          >
          <textarea
            class="outline-none appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6"
            required
            type="text"
            v-model="pos_res"
          />
        </div>
        <div
          class="w-full px-3 flex-nm xs:flex-nm sm:flex-nm md:flex-nm lg:flex-nm xl:flex-el"
        >
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            >Preferred Qualifications</label
          >
          <input
            class="outline-none appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6"
            required
            type="text"
            v-model="pref_qual"
          />
        </div>
        <div
          class="w-full px-3 flex-nm xs:flex-nm sm:flex-nm md:flex-nm lg:flex-nm xl:flex-el"
        >
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            >Minimum Qualifications</label
          >
          <textarea
            class="outline-none appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6"
            required
            type="text"
            v-model="min_qual"
          />
        </div>
        <div
          class="w-full px-3 flex-nm xs:flex-nm sm:flex-nm md:flex-nm lg:flex-nm xl:flex-el"
        >
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            >Additional Info</label
          >
          <input
            class="outline-none appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6"
            required
            type="text"
            v-model="add_info"
          />
        </div>
        <div
          class="w-full px-3 flex-nm xs:flex-nm sm:flex-nm md:flex-nm lg:flex-nm xl:flex-el"
        >
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            >Duration (in weeks)</label
          >
          <input
            class="outline-none appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6"
            required
            type="number"
            v-model="duration"
          />
        </div>
        <div
          class="w-full px-3 flex-nm xs:flex-nm sm:flex-nm md:flex-nm lg:flex-nm xl:flex-el"
        >
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            >Application Open Date</label
          >
          <input
            class="outline-none appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6"
            required
            type="date"
            v-model="app_open"
          />
        </div>
        <div
          class="w-full px-3 flex-nm xs:flex-nm sm:flex-nm md:flex-nm lg:flex-nm xl:flex-el"
        >
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            >Application Close Date</label
          >
          <input
            class="outline-none appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6"
            required
            type="date"
            v-model="app_close"
          />
        </div>
        <div
          class="w-full px-3 flex-nm xs:flex-nm sm:flex-nm md:flex-nm lg:flex-nm xl:flex-el"
        >
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            >Relevant SU Courses (control click to add multiple)</label
          >
          <select
            class="outline-none appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6"
            required
            v-model="courses_on_listing"
            multiple
          >
            <option
              v-for="(course, index) in su_courses"
              v-bind:key="index"
              v-bind:selected="course in courses_on_listing"
            >
              {{ course.course_num }} - {{ course.course_title }}
            </option>
          </select>
        </div>
        <div
          class="w-full px-3 flex-nm xs:flex-nm sm:flex-nm md:flex-nm lg:flex-nm xl:flex-el"
        >
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            >Tags</label
          >
          <select
            class="outline-none appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6"
            required
            v-model="tags_on_listing"
            multiple
          >
            <option
              v-for="(tag, index) in tags"
              v-bind:key="index"
              v-bind:selected="tag in tags_on_listing"
            >
              {{ tag }}
            </option>
          </select>
        </div>
        <div
          class="w-full px-3 flex-nm xs:flex-nm sm:flex-nm md:flex-nm lg:flex-nm xl:flex-el"
        >
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            >Application Link</label
          >
          <input
            class="outline-none appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6"
            required
            type="text"
            v-model="app_link"
          />
        </div>
      </div>
      <div class="flex items-center justify-center w-full mb-12">
        <label for="toogleA" class="flex items-center cursor-pointer">
          <div class="relative">
            <input
              id="toogleA"
              type="checkbox"
              class="sr-only"
              v-model="status"
            />
            <div class="w-10 h-4 bg-gray-400 rounded-full shadow-inner"></div>
            <div
              class="dot absolute w-6 h-6 bg-white rounded-full shadow -left-1 -top-1 transition"
            ></div>
          </div>
          <div v-if="status == true" class="ml-3 text-gray-600 font-medium">
            Listing Activated
          </div>
          <div v-else class="ml-3 text-gray-700 font-medium">
            Listing Deactivated
          </div>
        </label>
      </div>
      <button
        type="button"
        class="bg-primary hover:bg-primaryOffset text-white font-bold py-2 px-4 w-1/3 m-auto rounded flex justify-center items-center"
        @click="updateListing"
      >
        Update
      </button>
      <Modal
        v-if="show_modal"
        :ModalTitleProp="modal_title"
        :ModalCloseCallback="closeModal"
        :ModalMessageProp="modal_message"
      />
    </div>
  </form>
</template>

<script>
import { ref, onMounted } from "vue";
import Modal from "./Modal.vue";
export default {
  name: "EditListing",
  components: {
    Modal,
  },
  setup() {
    const id = ref(0);
    const position = ref("");
    const min_qual = ref("");
    const pref_qual = ref("");
    const pos_res = ref("");
    const add_info = ref("");
    const duration = ref("");
    const app_open = ref("");
    const app_close = ref("");
    const app_link = ref("");
    const status = ref(false);
    const su_courses = ref([]);
    const selected_courses = ref([]);
    const selected_tags = ref([]);
    const tags = ref([]);
    const tags_on_listing = ref([]);
    const courses_on_listing = ref([]);
    const show_modal = ref(false);
    const modal_title = ref("");
    const modal_message = ref("");
    const pending = ref("");
    const statusString = ref("");

    function closeModal() {
      show_modal.value = false;
    }

    function formatDate(dateToFormat) {
      let dateToReturn = "";
      if (dateToFormat != null) {
        if (dateToFormat.includes("-")) {
          let l = dateToFormat.split("-");
          if (l[0].length == 4) {
            dateToReturn = dateToFormat;
          } else {
            if (l[0] === "undefined" && l[l.length - 1] === "undefined") {
              let year = l[1];
              let month = l[2];
              let day = l[3];
              dateToReturn = year + "-" + month + "-" + day;
            } else {
              dateToReturn = l[2] + "-" + l[0] + "-" + l[1];
            }
          }
        } else if (dateToFormat.includes("/")) {
          let l = dateToFormat.split("/");
          if (l[0].length == 4) {
            dateToReturn = dateToFormat;
          } else {
            if (l[0] === "undefined" && l[l.length - 1] === "undefined") {
              let year = l[1];
              let month = l[2];
              let day = l[3];
              dateToReturn = year + "-" + month + "-" + day;
            } else {
              dateToReturn = l[2] + "-" + l[0] + "-" + l[1];
            }
          }
        }
      }
      return dateToReturn;
    }

    onMounted(async () => {
      let uri = window.location.search.substring(1);
      let params = new URLSearchParams(uri);
      let listing_id = params.get("id");
      let result = await fetch(
        `${process.env.SERVER_URL}/get-listing/${listing_id}`
      ).catch((error) => {
        console.log(error);
      });
      let listing = await result.json();
      let course_result = await fetch(
        `${process.env.SERVER_URL}/admin/get-all-courses`
      ).catch((error) => {
        console.log(error);
      });
      let all_courses = await course_result.json();

      let tag_result = await fetch(
        `${process.env.SERVER_URL}/admin/get-all-tags`
      ).catch((error) => {
        console.log(error);
      });
      let all_tags = await tag_result.json();
      tags.value = all_tags.tags;

      let l = listing.listing;
      console.log(listing);
      id.value = l.id;
      position.value = l.position;
      pos_res.value = l.pos_responsibility;
      min_qual.value = l.min_qualifications;
      pref_qual.value = l.pref_qualifications;
      add_info.value = l.additional_info;
      duration.value = l.duration;
      app_open.value = formatDate(l.app_open);
      app_close.value = formatDate(l.app_close);
      app_link.value = l.app_link;
      su_courses.value = all_courses.courses;
      tags_on_listing.value = listing.tags;
      courses_on_listing.value = listing.courses;
      console.log(tags_on_listing.value);
      console.log(courses_on_listing.value);
      statusString.value = l.status;
      status.value = l.status == "active" ? true : false;
    });
    async function set_active() {
      if (pending.value == "pending") {
        pending.value = "active";
        console.log(pending.value);
      } else {
        pending.value = "pending";
        console.log(pending.value);
      }
    }
    async function updateListing() {
      for (let i = 0; i < selected_courses.value.length; i++) {
        let course_num = selected_courses.value[i].split(" - ")[0];
        selected_courses.value[i] = course_num;
        console.log(selected_courses.value[i]);
      }
      const listing = {
        position_title: position.value,
        pos_responsibility: pos_res.value,
        min_qualifications: min_qual.value,
        pref_qualifications: pref_qual.value,
        additional_info: add_info.value,
        duration: duration.value,
        app_open: app_open.value,
        app_close: app_close.value,
        su_courses: courses_on_listing.value,
        tags: tags_on_listing.value,
        app_link: app_link.value,
        status: status.value == true ? "active" : "inactive",
      };

      await fetch(`${process.env.SERVER_URL}/admin/edit-listing/${id.value}`, {
        method: "PUT",
        mode: "cors",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(listing),
      }).then((res) => {
        if (res.status === 200) {
          show_modal.value = true;
          modal_title.value = "Update Successful!";
          modal_message.value =
            "You have successfully updated the information about this listing";
        } else {
          show_modal.value = true;
          modal_title.value = "Error!";
          modal_message.value =
            "There was an error with updating the information about this listing. Please try again!";
        }
      });
    }

    return {
      id,
      position,
      pos_res,
      min_qual,
      pref_qual,
      add_info,
      duration,
      app_open,
      app_close,
      app_link,
      status,
      statusString,
      su_courses,
      selected_courses,
      selected_tags,
      tags,
      show_modal,
      modal_title,
      modal_message,
      tags_on_listing,
      courses_on_listing,
      updateListing,
      closeModal,
    };
  },
};
</script>

<style>
input:checked ~ .dot {
  transform: translateX(100%);
  background-color: #48bb78;
}
</style>
