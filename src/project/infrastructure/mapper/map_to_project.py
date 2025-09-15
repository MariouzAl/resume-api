from src.project.domain.entities.project_category import ProjectCategory
from src.project.infrastructure.models.project import Project as ProjectModel
from src.project.domain.entities.project import Project as ProjectEntity


def map_to_project(model: ProjectModel):
    return ProjectEntity(
        id=model.id,
        project=model.project,
        builtWith=[skill.skill for skill in model.skills],
        categories=[ProjectCategory(id=cat.id, name=cat.name) for cat in model.categories] if model.categories is not None else [],
        shortDescription=model.shortDescription,
        fullDescription=model.fullDescription,
        start_date=model.start_date,
        end_date=model.end_date,
        cover=model.cover,
        images=[image.url for image in model.images],
        key=model.key,
        link=model.link,
        projectLink=model.projectLink,
        responsibilities=[resp.description for resp in  model.responsibilities],
        professional_experience_id=model.professional_experience.id if model.professional_experience is not None else None
    )
