from src.states.blogstate import BlogState
from langchain_core.messages import HumanMessage, SystemMessage
from src.states.blogstate import Blog


class BlogNode:
    """
    A class to represent the blog node
    """

    def __init__(self,llm):
        self.llm=llm

    def title_creation(self,state:BlogState):
        """
        Create the title for blog
        """

        if "topic" in state and state["topic"]:
            prompt="""
                    you are an expert blog content writer. Use Markdown formatting. Generate
                    a blog title for {topic}. This title should be creative and SEO friendly.
 
                    """
            system_message=prompt.format(topic=state["topic"])
            response=self.llm.invoke(system_message)
            return {"blog":{"title":response.content}}


    def content_generation(self,state:BlogState):
        """
        Create the content for blog
        """
        
        if "topic" in state and state["topic"]:
            system_prompt="""
                    you are an expert blog content writer. Use Markdown formatting. Generate
                    a detailed blog content with detailed breakdown for the {topic}. This title should be creative and SEO friendly.
         
                    """
            system_message=system_prompt.format(topic=state["topic"])
            response=self.llm.invoke(system_message)
            return {"blog":{"title":state["blog"]["title"],"content":response.content}}


    def translation(self,state:BlogState):
        """
        Translate the content to specified language
        """
        translation_prompt="""
        Translate the following content into {current_language}.
        - Maintain the orignal tone, style, and formatting.
        - Adapt cultural refrences and idioms to appropriate for {current_language}.

        ORIGNAL CONTENT:
        {blog_content}

        """

        blog_content=state["blog"]["content"]

        formatted_text = translation_prompt.format(
            current_language=state["current_language"],
            blog_content=blog_content
        )

        messages=[
            HumanMessage(content=formatted_text)

        ]
        translated_content= self.llm.with_structured_output(Blog).invoke(messages)

        return {"blog":translated_content}

    #def route(self,state:BlogState):
     #   return {"current_language": state["current_language"]}

    def route(self, state: BlogState):
        # FIX: Use .get() or simply pass state through without trying to access direct key index
        return {"current_language": state.get("current_language", "")}

    def route_decision(self, state: BlogState):
        """
        Route the content to the respective translation function.
        """

        if state["current_language"] == "hindi":
            return "hindi"
        elif state["current_language"] == "french":
            return "french"
        else:
            return state["current_language"]


        