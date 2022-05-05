<template>
  <section>
    <div class="container mx-auto">
      <div class="min-h-screen">
        <div
          class="mt-12 relative col-start-2 col-span-8 row-start-1 row-end-4 bg-gray-100 text-gray-500 text-lg font-bold text-center p-10 rounded-lg place-content-center"
        >
          <div class="flex flex-start">
            <div class="mx-auto my-auto py-4 h-1/2 w-3/4">
              Views by Job Type
              <div class="h-1/2 w-1/2 mx-auto">
                <vue3-chart-js
                  :id="viewsChart.id"
                  :type="viewsChart.type"
                  :data="viewsChart.data"
                  @before-render="beforeRenderLogic"
                ></vue3-chart-js>
              </div>
            </div>

            <div class="mx-auto my-auto py-4 h-1/2 w-3/4">
              Listings by Job Type
              <div class="h-1/2 w-1/2 mx-auto">
                <vue3-chart-js
                  :id="listingsChart.id"
                  :type="listingsChart.type"
                  :data="listingsChart.data"
                  @before-render="beforeRenderLogic"
                ></vue3-chart-js>
              </div>
            </div>
          </div>
        </div>
        <div
          class="mt-4 relative col-start-2 col-span-8 row-start-4 row-end-6 bg-gray-100 text-gray-500 text-lg font-bold text-center p-10 rounded-lg overflow-hidden pb-5"
        >
          <div class="my-auto center flex-wrap">
            Site Vists and New Listings
            <div class="mx-auto my-auto py-4 h-1/2 w-3/4">
              <vue3-chart-js
                :id="lineChart.id"
                :type="lineChart.type"
                :data="lineChart.data"
                @before-render="beforeRenderLogic"
              ></vue3-chart-js>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import PendingListingModule from "./PendingListingModule.vue";
import ContactInboxModule from "./ContactInbox.vue";
import Vue3ChartJs from "@j-t-mcc/vue3-chartjs";
import zoomPlugin from "chartjs-plugin-zoom";
import dataLabels from "chartjs-plugin-datalabels";
import { onMounted, ref, toRaw } from "vue"

Vue3ChartJs.registerGlobalPlugins([zoomPlugin]);

export default {
  name: "AdminDashboard",
  components: {
    Vue3ChartJs,
    PendingListingModule,
    ContactInboxModule,
  },
  setup() {

    const all_listings = ref([])
    const all_positions = ref([])
    const all_ids = ref([])
    const statistics = ref([])
    const all_companies = ref([])
    const stats_two = ref([])
    const stats_three = ref([])
    onMounted(async () => {
      let result = await fetch(
        `${process.env.SERVER_URL}/get-listings/active`
      ).catch((error) => {
        console.log(error);
      });
      let listings = await result.json();
      let arrOfObjects = Object.entries(listings).map((listing) => listing[1]);
      all_listings.value = arrOfObjects;
      for(let i = 0; i < arrOfObjects.length; i++) {
        all_ids.value.push(arrOfObjects[i].listing.id);
      }
      let arr = JSON.parse(JSON.stringify(all_ids.value));
      console.log(arr)
      for(let i = 0; i < arrOfObjects.length; i++) {
        all_companies.value.push(all_listings.value[i].client);
      }
      let occurrences = toRaw(all_companies.value).reduce(function (acc, curr) {
        return acc[curr] ? ++acc[curr] : acc[curr] = 1, acc
      }, {});
      for(let i = 0; i < arr.length; i++) {
        let result2 = await fetch(
          `${process.env.SERVER_URL}/get-statistics/${arr[i]}`
        ).catch((error) => {
          console.log(error);
        });
        let response = await result2.json();
        statistics.value.push(Object.entries(response).map((response) => response[1])[1])
        //console.log(Object.entries(response).map((response) => response[1]))
      }
      console.log(JSON.parse(JSON.stringify(statistics.value)))
      for(let i = 0; i < arrOfObjects.length; i++) {
        console.log(all_listings.value[i].listing.position)
        all_positions.value.push(all_listings.value[i].listing.position)
      }
      for(let j = 0; j < (Object.keys(toRaw(occurrences)).length); j++) {
        stats_two.value.push(Object.keys(toRaw(occurrences))[j])
        stats_three.value.push(Object.values(toRaw(occurrences))[j])
      }
      console.log(Object.keys(toRaw(occurrences)));
    });
    let temp2 = toRaw(all_positions.value)
    let temp1 = toRaw(statistics.value)
    let comps = toRaw(stats_two.value)
    let comps_listings = toRaw(stats_three.value)

    const viewsChart = {
      id: "doughnut",
      type: "doughnut",
      data: {
        //but in the data object it isnt recognized as an array of strings
        labels: temp2,
        datasets: [
          {
            backgroundColor: [
              "#41B883",
              "#E46651",
              "#00D8FF",
              "#DD1B16",
            ],
            //same with ints
            data: temp1,
          },
        ],
      },
    };
    const listingsChart = {
      id: "doughnut",
      type: "doughnut",
      data: {
        labels: comps,
        datasets: [
          {
            backgroundColor: [
              "#E46651",
              "#00D8FF",
              "#41B883",
            ],
            data: comps_listings,
          },
        ],
      },
    };
    const lineChart = {
      type: "line",
      // locally registered and available for this chart
      plugins: [dataLabels],
      data: {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December",
        ],
        datasets: [
          {
            label: "New Listings",
            data: [15, 13, 14, 10, 5, 3, 4, 9, 15, 20, 25, 22],
            fill: false,
            borderColor: "#41B883",
            backgroundColor: "black",
          },
          {
            label: "Site Visits",
            data: [20, 28, 41, 35, 30, 10, 15, 10, 25, 30, 22, 35],
            fill: false,
            borderColor: "#00D8FF",
            tension: 0.5,
            backgroundColor: "blue",
          },
        ],
      },
      options: {
        plugins: {
          zoom: {
            zoom: {
              wheel: {
                enabled: true,
              },
              pinch: {
                enabled: true,
              },
              mode: "y",
            },
          },
          datalabels: {
            backgroundColor: function (context) {
              return context.dataset.backgroundColor;
            },
            borderRadius: 4,
            color: "white",
            font: {
              weight: "bold",
            },
            formatter: Math.round,
            padding: 6,
          },
          title: {
            display: true,
            text: "Custom Chart Title",
            padding: {
              top: 10,
              bottom: 30,
            },
          },
        },
      },
    };

    const beforeRenderLogic = (event) => {
      //...
      //if(a === b) {
      //  event.preventDefault()
      //}
    };

    return {
      viewsChart,
      listingsChart,
      lineChart,
      beforeRenderLogic,
    };
  },
};
</script>
