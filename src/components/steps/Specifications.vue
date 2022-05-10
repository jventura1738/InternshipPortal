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
            for="grid-internship-position-title"
          >
            Position Title
          </label>
          <input
            class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6"
            required=""
            id="grid-company-name"
            type="text"
            placeholder="Software Developer Intern"
            v-model="positionTitle"
            @change="titleChange"
          />
        </div>
        <div class="md:w-1/2 px-3">
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2"
            for="grid-minimum-qualifications"
          >
            Minimum Qualifications
          </label>
          <textarea
            class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 resize-none"
            rows="6"
            required
            id="grid-minimum-qualifications"
            type="text"
            placeholder="- Bachelor's student majoring in Computer Science or a related field
- Programming experience in C, C++, Java, JavaScript or Python
            "
            v-model="minQualifications"
            @change="minQualChange"
          />
        </div>
      </div>
      <div class="-mx-3 md:flex mb-6">
        <div class="md:w-full px-3">
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2"
            for="grid-preferred-qualifications"
          >
            Preferred Qualifications
          </label>
          <textarea
            class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 resize-none"
            rows="6"
            required=""
            id="grid-preferred-qualifications"
            type="text"
            placeholder="- Advanced degree in Computer Science, Computer Engineering, Electrical Engineering or related field
- Proficient in a scripting language, C/C++ programming and software design skills
            "
            v-model="prefQualifications"
            @change="prefQualChange"
          />
        </div>
      </div>
      <div class="-mx-3 md:flex mb-2">
        <div class="md:w-full px-3">
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2"
            for="grid-position-responsibilities"
          >
            Position Responsibilities
          </label>
          <textarea
            class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 resize-none"
            rows="6"
            required=""
            id="grid-position-responsibilities"
            type="text"
            placeholder="- Fulfill tasks set out by supervisors from several departments
- Attend meetings and take minutes
- Perform research at a supervisor's request
            "
            v-model="positionResponsibilities"
            @change="posResChange"
          />
        </div>
        <div class="md:w-full px-3">
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            for="grid-additional-information"
          >
            Additional Information
          </label>
          <textarea
            class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6 resize-none"
            rows="4"
            required=""
            id="grid-additional-information"
            type="text"
            placeholder="Any additional information about internship"
            v-model="additionalInfo"
            @change="addInfoChange"
          />
        </div>
        <div class="md:w-full px-3">
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            for="grid-duration"
          >
            Duration (in weeks)
          </label>
          <input
            class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6 resize-none"
            required=""
            id="grid-duration"
            type="number"
            placeholder="8"
            v-model="duration"
            @change="durationChange"
          />
        </div>
        <div class="md:w-full px-3">
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            for="grid-app-open"
          >
            Application Open Date
          </label>
          <input
            class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6 resize-none"
            required=""
            id="grid-duration"
            type="date"
            placeholder="01/01/2021"
            v-model="app_open"
            @change="appOpenChange"
          />
        </div>
        <div class="md:w-full px-3">
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            for="grid-app-close"
          >
            Application Close Date
          </label>
          <input
            class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6 resize-none"
            required=""
            id="grid-app-close"
            type="date"
            placeholder="01/01/2022"
            v-model="app_close"
            @change="appCloseChange"
          />
        </div>
        <div class="md:w-1/2 px-3 mb-6 md:mb-0">
          <label
            class="block uppercase tracking-wide text-grey-darker text-xs font-bold mb-2 mt-6"
            for="grid-internship-application-link"
          >
            Application Link
          </label>
          <input
            class="appearance-none block w-full bg-grey-lighter text-grey-darker border border-grey-lighter rounded py-3 px-4 mb-6"
            required=""
            id="grid-application-link"
            type="text"
            placeholder="https://www.example.com/application"
            v-model="app_link"
            @change="appLinkChange"
          />
        </div>
      </div>
    </div>
  </form>
</template>

<script>
import { ref, toRefs } from "vue";
export default {
  name: "Specifications",
  props: {
    titleChangedCallback: Function,
    minQualChangedCallback: Function,
    prefQualChangedCallback: Function,
    posResChangedCallback: Function,
    addInfoChangedCallback: Function,
    durationChangedCallback: Function,
    appOpenChangedCallback: Function,
    appCloseChangedCallback: Function,
    appLinkChangedCallback: Function,
  },
  setup(props) {
    const {
      titleChangedCallback,
      minQualChangedCallback,
      prefQualChangedCallback,
      posResChangedCallback,
      addInfoChangedCallback,
      durationChangedCallback,
      appOpenChangedCallback,
      appCloseChangedCallback,
      appLinkChangedCallback,
    } = toRefs(props);
    const positionTitle = ref("");
    const minQualifications = ref("");
    const prefQualifications = ref("");
    const positionResponsibilities = ref("");
    const additionalInfo = ref("");
    const duration = ref(0);
    const app_open = ref("");
    const app_close = ref("");
    const app_link = ref("");
    function titleChange() {
      titleChangedCallback.value(positionTitle.value);
    }
    function minQualChange() {
      minQualChangedCallback.value(minQualifications.value);
    }
    function prefQualChange() {
      prefQualChangedCallback.value(prefQualifications.value);
    }
    function posResChange() {
      posResChangedCallback.value(positionResponsibilities.value);
    }
    function addInfoChange() {
      addInfoChangedCallback.value(additionalInfo.value);
    }
    function durationChange() {
      durationChangedCallback.value(duration.value);
    }
    function appOpenChange() {
      appOpenChangedCallback.value(app_open.value);
    }
    function appCloseChange() {
      appCloseChangedCallback.value(app_close.value);
    }
    function appLinkChange() {
      appLinkChangedCallback.value(app_link.value);
    }
    return {
      positionTitle,
      minQualifications,
      prefQualifications,
      positionResponsibilities,
      additionalInfo,
      duration,
      app_open,
      app_close,
      app_link,
      titleChange,
      minQualChange,
      prefQualChange,
      posResChange,
      addInfoChange,
      durationChange,
      appOpenChange,
      appCloseChange,
      appLinkChange,
    };
  },
};
</script>

<style>
select:invalid {
  color: rgba(156, 163, 175, 1);
}
</style>
