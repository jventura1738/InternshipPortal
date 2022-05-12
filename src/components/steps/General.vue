<!-- TODO: INPUT VALIDATE THIS -->
<template>
  <form>
    <div
      class="shadow-xl border-2 rounded px-8 pt-6 pb-8 mb-4 flex flex-col my-2 m-auto w-3/4"
    >
      <div class="-mx-3 md:flex mb-6">
        <div class="md:w-1/2 px-3 mb-6 md:mb-0">
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            for="grid-company-name"
          >
            Company Name <span class="text-red-600">*</span>
          </label>
          <input
            class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-3"
            @change="nameChange"
            required=""
            id="grid-company-name"
            type="text"
            placeholder="Amazon"
            v-model="companyName"
          />
        </div>
        <div class="md:w-1/2 px-3">
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2"
            for="grid-address"
          >
            Company HQ Address <span class="text-red-600">*</span>
          </label>
          <!-- Make this autocomplete properly -->
          <input
            class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4"
            @change="addressChange"
            required
            id="grid-address"
            type="text"
            placeholder="123 Apple St."
            v-model="companyAddress"
          />
        </div>
      </div>
      <div class="-mx-3 md:flex mb-6">
        <div class="md:w-full px-3">
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2"
            for="grid-city"
          >
            City <span class="text-red-600">*</span>
          </label>
          <input
            class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4"
            @change="cityChange"
            required=""
            id="grid-city"
            type="text"
            placeholder="Seattle"
            v-model="companyCity"
          />
        </div>
      </div>
      <div class="-mx-3 md:flex mb-2">
        <div class="md:w-1/2 px-3">
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2"
            for="grid-state"
          >
            State <span class="text-red-600">*</span>
          </label>
          <div class="relative">
            <select
              class="block appearance-none w-full bg-white border border-grey-lighter text-grey-darker py-3 px-4 pr-8 rounded"
              @change="stateChange"
              required=""
              id="grid-state"
              v-model="companyState"
            >
              <option disable hidden value="">Select State</option>
              <option v-for="state in states" :key="state.abbreviation">
                {{ state.name }}
              </option>
            </select>
          </div>
        </div>
        <div class="md:w-1/2 px-3">
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            for="grid-zip"
          >
            Zip <span class="text-red-600">*</span>
          </label>
          <input
            class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6"
            @change="zipChange"
            required=""
            id="grid-zip"
            type="text"
            placeholder="12345"
            v-model="companyZip"
          />
        </div>
        <div class="px-3">
          <span class="text-red-600">*</span> Required fields
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import { ref, toRefs } from "vue";
// TODO: Change input outline colors
export default {
  name: "General",
  props: {
    nameChangedCallback: Function,
    addressChangedCallback: Function,
    cityChangedCallback: Function,
    stateChangedCallback: Function,
    zipChangedCallback: Function,
  },
  setup(props) {
    const {
      nameChangedCallback,
      addressChangedCallback,
      cityChangedCallback,
      stateChangedCallback,
      zipChangedCallback,
    } = toRefs(props);
    const states = ref([
      {
        name: "Alabama",
        abbreviation: "AL",
      },
      {
        name: "Alaska",
        abbreviation: "AK",
      },
      {
        name: "American Samoa",
        abbreviation: "AS",
      },
      {
        name: "Arizona",
        abbreviation: "AZ",
      },
      {
        name: "Arkansas",
        abbreviation: "AR",
      },
      {
        name: "California",
        abbreviation: "CA",
      },
      {
        name: "Colorado",
        abbreviation: "CO",
      },
      {
        name: "Connecticut",
        abbreviation: "CT",
      },
      {
        name: "Delaware",
        abbreviation: "DE",
      },
      {
        name: "District Of Columbia",
        abbreviation: "DC",
      },
      {
        name: "Federated States Of Micronesia",
        abbreviation: "FM",
      },
      {
        name: "Florida",
        abbreviation: "FL",
      },
      {
        name: "Georgia",
        abbreviation: "GA",
      },
      {
        name: "Guam",
        abbreviation: "GU",
      },
      {
        name: "Hawaii",
        abbreviation: "HI",
      },
      {
        name: "Idaho",
        abbreviation: "ID",
      },
      {
        name: "Illinois",
        abbreviation: "IL",
      },
      {
        name: "Indiana",
        abbreviation: "IN",
      },
      {
        name: "Iowa",
        abbreviation: "IA",
      },
      {
        name: "Kansas",
        abbreviation: "KS",
      },
      {
        name: "Kentucky",
        abbreviation: "KY",
      },
      {
        name: "Louisiana",
        abbreviation: "LA",
      },
      {
        name: "Maine",
        abbreviation: "ME",
      },
      {
        name: "Marshall Islands",
        abbreviation: "MH",
      },
      {
        name: "Maryland",
        abbreviation: "MD",
      },
      {
        name: "Massachusetts",
        abbreviation: "MA",
      },
      {
        name: "Michigan",
        abbreviation: "MI",
      },
      {
        name: "Minnesota",
        abbreviation: "MN",
      },
      {
        name: "Mississippi",
        abbreviation: "MS",
      },
      {
        name: "Missouri",
        abbreviation: "MO",
      },
      {
        name: "Montana",
        abbreviation: "MT",
      },
      {
        name: "Nebraska",
        abbreviation: "NE",
      },
      {
        name: "Nevada",
        abbreviation: "NV",
      },
      {
        name: "New Hampshire",
        abbreviation: "NH",
      },
      {
        name: "New Jersey",
        abbreviation: "NJ",
      },
      {
        name: "New Mexico",
        abbreviation: "NM",
      },
      {
        name: "New York",
        abbreviation: "NY",
      },
      {
        name: "North Carolina",
        abbreviation: "NC",
      },
      {
        name: "North Dakota",
        abbreviation: "ND",
      },
      {
        name: "Northern Mariana Islands",
        abbreviation: "MP",
      },
      {
        name: "Ohio",
        abbreviation: "OH",
      },
      {
        name: "Oklahoma",
        abbreviation: "OK",
      },
      {
        name: "Oregon",
        abbreviation: "OR",
      },
      {
        name: "Palau",
        abbreviation: "PW",
      },
      {
        name: "Pennsylvania",
        abbreviation: "PA",
      },
      {
        name: "Puerto Rico",
        abbreviation: "PR",
      },
      {
        name: "Rhode Island",
        abbreviation: "RI",
      },
      {
        name: "South Carolina",
        abbreviation: "SC",
      },
      {
        name: "South Dakota",
        abbreviation: "SD",
      },
      {
        name: "Tennessee",
        abbreviation: "TN",
      },
      {
        name: "Texas",
        abbreviation: "TX",
      },
      {
        name: "Utah",
        abbreviation: "UT",
      },
      {
        name: "Vermont",
        abbreviation: "VT",
      },
      {
        name: "Virgin Islands",
        abbreviation: "VI",
      },
      {
        name: "Virginia",
        abbreviation: "VA",
      },
      {
        name: "Washington",
        abbreviation: "WA",
      },
      {
        name: "West Virginia",
        abbreviation: "WV",
      },
      {
        name: "Wisconsin",
        abbreviation: "WI",
      },
      {
        name: "Wyoming",
        abbreviation: "WY",
      },
    ]);
    const companyName = ref("");
    const companyAddress = ref("");
    const companyCity = ref("");
    const companyState = ref("");
    const companyZip = ref("");
    function nameChange() {
      nameChangedCallback.value(companyName.value);
    }
    function addressChange() {
      addressChangedCallback.value(companyAddress.value);
    }
    function cityChange() {
      cityChangedCallback.value(companyCity.value);
    }
    function stateChange() {
      stateChangedCallback.value(companyState.value);
    }
    function zipChange() {
      zipChangedCallback.value(companyZip.value);
    }

    return {
      states,
      companyName,
      companyAddress,
      companyCity,
      companyState,
      companyZip,
      nameChange,
      addressChange,
      cityChange,
      stateChange,
      zipChange,
    };
  },
};
</script>

<style>
select:invalid {
  color: rgba(156, 163, 175, 1);
}
</style>
