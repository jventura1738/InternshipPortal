<template>
  <div class="sm:flex sm:items-center justify-between mx-48 mt-12">
    <div class="flex space-x-1 mt-10">
      <button
        type="button"
        class="p-1.5 text-gray-700 rounded bg-gray-100"
        @click="toggleTableView"
      >
        <span class="sr-only"> View as Table </span>

        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="w-5 h-5"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6h16M4 10h16M4 14h16M4 18h16"
          />
        </svg>
      </button>

      <button
        type="button"
        class="p-1.5 text-gray-700 rounded bg-gray-100"
        @click="toggleGridView"
      >
        <span class="sr-only"> View as Grid </span>

        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="w-5 h-5"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
        >
          <path
            stroke-linecap="round"
            stroke-linejoin="round"
            stroke-width="2"
            d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"
          />
        </svg>
      </button>
    </div>
    
    <div class="flex items-center">
    <div class="pt-2 mt-10 relative mx-auto text-gray-60">
      <input
        class="border-2 border-gray-300 bg-white h-10 w-72 px-5 pr-16 rounded-lg text-sm focus:outline-none"
        type="text"
        name="search"
        :placeholder="`Search by ${filterValue}`"
        v-model="searchTerm"
        @input="filterListings"
      />
      <button type="submit" class="absolute right-0 top-0 mt-5 mr-4">
        <svg
          class="text-gray-600 h-4 w-4 fill-current"
          xmlns="http://www.w3.org/2000/svg"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          version="1.1"
          id="Capa_1"
          x="0px"
          y="0px"
          viewBox="0 0 56.966 56.966"
          style="enable-background: new 0 0 56.966 56.966"
          xml:space="preserve"
          width="512px"
          height="512px"
        >
          <path
            d="M55.146,51.887L41.588,37.786c3.486-4.144,5.396-9.358,5.396-14.786c0-12.682-10.318-23-23-23s-23,10.318-23,23  s10.318,23,23,23c4.761,0,9.298-1.436,13.177-4.162l13.661,14.208c0.571,0.593,1.339,0.92,2.162,0.92  c0.779,0,1.518-0.297,2.079-0.837C56.255,54.982,56.293,53.08,55.146,51.887z M23.984,6c9.374,0,17,7.626,17,17s-7.626,17-17,17  s-17-7.626-17-17S14.61,6,23.984,6z"
          />
        </svg>
      </button>
    </div>
    </div>
  
   
    <form action="" class="flex mt-2 sm:mt-0">
      <div>
        <BrowseFilterDropdown :changeFilter="updateFilter" />
      </div>

      <div class="ml-4">
        <BrowseSortDropdown :changeFilter="sortListings" />
      </div>
    </form>
   
  </div>
  
  <div v-if="tableViewToggle">
    <ListingTable :listings="filtered_listings" />
  </div>
  <div v-if="gridViewToggle" class="mt-14">
    <BrowseListingCard :listings="filtered_listings" />
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import BrowseListingCard from "../components/BrowseListingCard.vue";
import ListingTable from "../components/ListingTable.vue";
import BrowseFilterDropdown from "../components/BrowseFilterDropdown.vue";
import BrowseSortDropdown from "../components/BrowseSortDropdown.vue";
export default {
  name: "Searchbar",
  components: {
    ListingTable,
    BrowseListingCard,
    BrowseFilterDropdown,
    BrowseSortDropdown,
  },
  setup() {
    const tableViewToggle = ref(true);
    const gridViewToggle = ref(false);
    const all_listings = ref([]);
    const filtered_listings = ref([]);
    const searchTerm = ref("");
    const filterValue = ref("title");
    const sortValue = ref("title-asc");

    onMounted(async () => {
      let result = await fetch(
        `${process.env.SERVER_URL}/get-listings/active`
      ).catch((error) => {
        console.log(error);
      });
      let listings = await result.json();
      console.log(listings);
      all_listings.value = Object.entries(listings);
      filtered_listings.value = Object.entries(listings);
      sortListings(sortValue.value);
    });

    function toggleTableView() {
      gridViewToggle.value = false;
      tableViewToggle.value = true;
    }

    function toggleGridView() {
      tableViewToggle.value = false;
      gridViewToggle.value = true;
    }

    function updateFilter(filter) {
      filterValue.value = filter;
    }

    function filterListings() {
      if (searchTerm.value == "") {
        filtered_listings.value = all_listings.value;
      } else {
        switch (filterValue.value) {
          case "title":
            filtered_listings.value = all_listings.value.filter((listing) => {
              if (
                listing[1].listing.position
                  .toLowerCase()
                  .includes(searchTerm.value.toLowerCase())
              ) {
                return listing;
              }
            });
            break;
          case "company":
            filtered_listings.value = all_listings.value.filter((listing) => {
              if (
                listing[1].client
                  .toLowerCase()
                  .includes(searchTerm.value.toLowerCase())
              ) {
                return listing;
              }
            });
            break;
          case "tags":
            filtered_listings.value = all_listings.value.filter((listing) => {
              let flag = false;
              listing[1].tags.forEach((tag) => {
                if (
                  tag.toLowerCase().includes(searchTerm.value.toLowerCase())
                ) {
                  flag = true;
                }
              });
              if (flag == true) return listing;
            });
            break;
          case "courses":
            filtered_listings.value = all_listings.value.filter((listing) => {
              let flag = false;
              listing[1].courses.forEach((course) => {
                if (
                  course.toLowerCase().includes(searchTerm.value.toLowerCase())
                ) {
                  flag = true;
                }
              });
              if (flag == true) return listing;
            });
            break;
        }
      }
    }

    function sortListings(sort) {
      sortValue.value = sort;
      switch (sortValue.value) {
        case "title-asc":
          filtered_listings.value = filtered_listings.value.sort((a, b) => {
            if (
              a[1].listing.position.toLowerCase()[0] <
              b[1].listing.position.toLowerCase()[0]
            )
              return -1;
            if (
              a[1].listing.position.toLowerCase()[0] >
              b[1].listing.position.toLowerCase()[0]
            )
              return 1;
            return 0;
          });
          break;
        case "title-desc":
          filtered_listings.value = filtered_listings.value.sort((a, b) => {
            if (
              a[1].listing.position.toLowerCase()[0] >
              b[1].listing.position.toLowerCase()[0]
            )
              return -1;
            if (
              a[1].listing.position.toLowerCase()[0] <
              b[1].listing.position.toLowerCase()[0]
            )
              return 1;
            return 0;
          });
          break;
        case "company-asc":
          filtered_listings.value = filtered_listings.value.sort((a, b) => {
            if (a[1].client.toLowerCase()[0] < b[1].client.toLowerCase()[0])
              return -1;
            if (a[1].client.toLowerCase()[0] > b[1].client.toLowerCase()[0])
              return 1;
            return 0;
          });
          break;
        case "company-desc":
          filtered_listings.value = filtered_listings.value.sort((a, b) => {
            if (a[1].client.toLowerCase()[0] > b[1].client.toLowerCase()[0])
              return -1;
            if (a[1].client.toLowerCase()[0] < b[1].client.toLowerCase()[0])
              return 1;
            return 0;
          });
          break;
        case "wage-asc":
          break;
        case "wage-desc":
          break;
      }
    }

    return {
      tableViewToggle,
      gridViewToggle,
      toggleTableView,
      toggleGridView,
      filterListings,
      sortListings,
      updateFilter,
      all_listings,
      filtered_listings,
      searchTerm,
      filterValue,
      sortValue,
    };
  },
};
</script>
