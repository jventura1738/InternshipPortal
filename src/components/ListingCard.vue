<template>
  <div class="flex flex-wrap">
    <div
      v-for="listing in listings"
      class="sm:flex-sm md:flex-md lg:flex-lg last:flex-el flex-nm m-4 shadow-lg rounded-xl bg-gray-100"
      :key="listing[1].listing.id"
    >
      <div class="relative">
        <div class="absolute top-0 right-0 p-4">
          <Star :id="listing[1].listing.id" />
        </div>
        <div class="p-4">
          <svg
            xmlns="http://www.w3.org/2000/svg"
            class="h-6 w-6 cursor-pointer"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
            stroke-width="2"
            className="cursor-pointer"
            @click="editListing(listing[1].listing.id)"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"
            />
          </svg>
        </div>
      </div>
      <div></div>
      <div class="px-6 py-4">
        <div class="font-bold text-xl mb-2">
          {{ listing[1].listing.position }}
        </div>
        <p class="text-black font-semibold text-base">
          Client:
          <span class="text-gray-700 font-normal">{{ listing[1].client }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Minimum Qualifications:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.min_qualifications
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Preferred Qualifications:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.pref_qualifications
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Additional Info:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.additional_info
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Responsibilities:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.pos_responsibility
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Duration:
          <span class="text-gray-700 font-normal"
            >{{
              listing[1].listing.duration != null
                ? listing[1].listing.duration + " weeks"
                : ""
            }}
          </span>
        </p>
        <p class="text-black font-semibold text-base">
          Open Date:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.app_open
          }}</span>
        </p>
        <p class="text-black font-semibold text-base">
          Close Date:
          <span class="text-gray-700 font-normal">{{
            listing[1].listing.app_close
          }}</span>
        </p>
      </div>
      <div class="px-6 pt-4 pb-2">
        <span
          class="inline-block rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
          :class="
            listing[1].listing.status == 'active'
              ? 'bg-green-300'
              : listing[1].listing.status == 'rejected'
              ? 'bg-red-300'
              : listing[1].listing.status == 'pending'
              ? 'bg-yellow-300'
              : listing[1].listing.status == 'inactive'
              ? 'bg-blue-300'
              : 'bg-gray-200'
          "
          >status: {{ listing[1].listing.status }}</span
        >
        <span
          class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
          >client_id: {{ listing[1].listing.client_id }}</span
        >
        <span
          class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
          >listing_id: {{ listing[1].listing.id }}</span
        >
      </div>
    </div>
  </div>
</template>

<script>
import Star from "./Star.vue";
export default {
  name: "ListingCard",
  props: ["listings"],
  components: {
    Star,
  },
  setup() {
    function toListingPage(listing_id) {
      window.location.href = `/admin/listing/${listing_id}`;
    }
    function editListing(listing_id) {
      window.location.href = `/admin/edit/listing?id=${listing_id}`;
    }
    return {
      toListingPage,
      editListing,
    };
  },
};
</script>
